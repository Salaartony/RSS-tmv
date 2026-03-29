import os
import re
import random
import asyncio
import requests
import cloudscraper
from pyrogram import Client
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin
from database import tmv_collection, add_tmv
from configs import TMV_URL, BOT_TAG, TMV_TORRENT, TMV_LEECH_GRP, TMV_MIRROR_GRP, TMV_TORRENT_THUMB, SIZE_LIMIT_GB

# ================= Thumbnail Setup =================
tmvthumb_path = "/tmp/tmv_torrent_thumb.jpg"
if not os.path.exists(tmvthumb_path):
    try:
        resp = requests.get(TMV_TORRENT_THUMB, timeout=15)
        resp.raise_for_status()
        with open(tmvthumb_path, "wb") as f:
            f.write(resp.content)
        print(f"✅ TMV thumbnail ready")
    except Exception as e:
        print(f"⚠️ Thumbnail failed: {e}")
        tmvthumb_path = None

# ================= Utilities =================
def clean_filename(name: str) -> str:
    name = unquote(name.strip())
    name = re.sub(r'^\s*(www\.[^-\s]+[\s-]*)+', '', name, flags=re.I)
    name = re.sub(r'^\s*(\S*TamilMV\S*[\s-]*)+', '', name, flags=re.I)
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    if not name.startswith(BOT_TAG):
        name = f"{BOT_TAG} - {name}"
    return name.strip()

def fix_url(href: str) -> str:
    return href if href.startswith("http") else urljoin(TMV_URL, href)

def download_file(scraper, url: str, filename: str) -> bool:
    try:
        response = scraper.get(url, stream=True, timeout=60)
        response.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk: f.write(chunk)
        return os.path.getsize(filename) > 0
    except:
        return False

# ================= Telegram Upload =================
async def send_torrent(user: Client, file_path, category, file_name, file_url, magnet, size_mb=0):
    clean_name = os.path.basename(file_path)
    caption = f"<b>{clean_name}\n\n#{category}\n\nPowered By ✨ {BOT_TAG}</b>"

    async def safe_send(chat_id, reply_cmd=None):
        try:
            msg = await user.send_document(
                chat_id=chat_id,
                document=file_path,
                caption=caption,
                thumb=tmvthumb_path if tmvthumb_path and os.path.exists(tmvthumb_path) else None,
            )
            if reply_cmd:
                await user.send_message(chat_id=chat_id, text=reply_cmd, reply_to_message_id=msg.id)
        except Exception as e:
            print(f"⚠️ Send failed: {e}")

    await safe_send(TMV_TORRENT)
    await safe_send(TMV_LEECH_GRP, reply_cmd="/qbleech")
    await safe_send(TMV_MIRROR_GRP, reply_cmd="/qbmirror")

    await add_tmv(file_name, file_url, magnet, size_mb)

# ================= TamilMV Scraper =================
async def tmv_scraper(user: Client):
    scraper = cloudscraper.create_scraper()
    print("🔍 Scraping TamilMV...")

    try:
        resp = scraper.get(TMV_URL, timeout=30)
        soup = BeautifulSoup(resp.text, "html.parser")
        topics = [fix_url(a["href"]) for a in soup.find_all("a", href=True) if "topic" in a["href"]][:39]
        for topic_url in topics:
            await asyncio.sleep(random.uniform(2, 4))
            try:
                topic_html = scraper.get(topic_url, timeout=30).text
                topic_soup = BeautifulSoup(topic_html, "html.parser")
                posts = topic_soup.find_all("div", class_="cPost_contentWrap")
                for post in posts:
                    for a in post.find_all("a", href=True):
                        if "torrent" in a.text.lower() and "applications" in a["href"]:
                            href = fix_url(a["href"])
                            if await tmv_collection.find_one({"file_url": href}):
                                continue

                            size_mb = 0
                            for sib in a.find_all_next(string=True, limit=6):
                                match = re.search(r"(\d+(\.\d+)?)\s*(gb|mb)", str(sib), re.I)
                                if match:
                                    val = float(match.group(1))
                                    unit = match.group(3).lower()
                                    size_mb = val * 1024 if unit == "gb" else val
                                    break

                            if SIZE_LIMIT_GB and size_mb > SIZE_LIMIT_GB * 1024:
                                continue

                            filename = clean_filename(a.text)
                            if not filename.endswith(".torrent"): filename += ".torrent"
                            if await asyncio.to_thread(download_file, scraper, href, filename):
                                await send_torrent(user, filename, "Movies", filename, href, href, size_mb)
                                if os.path.exists(filename): os.remove(filename)

            except: continue
    except Exception as e:
        print(f"🛑 Error: {e}")
