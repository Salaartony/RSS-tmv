
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<p align="center">
  <img src="https://i.ibb.co/JwSgd5zG/photo-2025-09-22-02-47-57-7570268308927152180.jpg" alt="SMD Logo">
</p>
<h2 align="center">
  「 sᴍᴅ ʀss sᴄʀᴀᴘᴘᴇʀ ʙᴏᴛ 」
</h2>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">


<p align="center">
  <b>Automated RSS + Torrent Scraper for TamilMV</b><br>
  <sub>Built with ❤️ using Pyrogram • CloudScraper • MongoDB</sub>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  </a>
  <a href="https://docs.pyrogram.org/">
    <img src="https://img.shields.io/badge/Pyrogram-v2.x-brightgreen?style=for-the-badge&logo=telegram">
  </a>
  <a href="https://render.com/">
    <img src="https://img.shields.io/badge/Deploy-Render-orange?style=for-the-badge&logo=render">
  </a>
  <a href="https://www.koyeb.com/">
    <img src="https://img.shields.io/badge/Deploy-Koyeb-purple?style=for-the-badge&logo=koyeb">
  </a>
  <a href="https://github.com/yourusername/tamilmv-scraper/stargazers">
    <img src="https://img.shields.io/github/stars/yourusername/tamilmv-scraper?style=for-the-badge&logo=github">
  </a>
</p>

---

## 🌊 Overview

The **TamilMV Scraper Bot** automatically monitors the latest posts on [1TamilMV.land](https://www.1tamilmv.land/), fetches torrent files, and uploads them directly to your **Telegram Channel or Group** — all hands-free!

It’s built for **24/7 automation**, works flawlessly on **Koyeb**, **Render**, **Railway**, or any **VPS**, and includes a **keep-alive web server** for free hosting deployments.

---

## ⚙️ Features

✅ **Automatic TamilMV Scraper**  
Continuously fetches new torrent topics and avoids reposts.  

📥 **Cloudflare-Bypass Downloader**  
Downloads protected files using `cloudscraper`.  

🤖 **Telegram Auto Uploader**  
Uploads torrents with caption, category, and thumbnail.  

🧠 **MongoDB Tracking**  
Prevents duplicate uploads intelligently.  

🖼️ **Custom Thumbnail Support**  
Adds a brand thumbnail to every Telegram post.  

🌐 **Built-in Web Server**  
Keeps the app alive even on free hosting (Koyeb/Render).  

🚀 **Async, Fault-Tolerant Design**  
Non-blocking tasks with retry logic and error recovery.  

---

## 🗂️ Project Structure

tamilmv_scraper/ │ ├── bot.py              # Main entry (Pyrogram client + web server) ├── configs.py          # Loads environment variables ├── database.py         # MongoDB setup & duplicate tracker ├── tamilmv.py          # TamilMV scraping & upload logic ├── thumbnail.jpg       # Custom thumbnail for Telegram uploads ├── requirements.txt    # Python dependencies └── .env                # Private environment variables

---

## 🚀 Setup & Deployment

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tamilmv-scraper.git
cd tamilmv-scraper

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token
MONGO_URI=your_mongodb_uri

TMV_URL=https://www.1tamilmv.land/
TMV_TORRENT=-100xxxxxxxxxx
TMV_LEECH_GRP=-100xxxxxxxxxx
TMV_MIRROR_GRP=-100xxxxxxxxxx
TMV_TORRENT_THUMB=https://example.com/thumb.jpg
BOT_TAG=⚡YourBotName⚡

4️⃣ Run the Bot

python3 bot.py


---

☁️ One-Click Deploy

<p align="center">
  <a href="https://render.com/deploy?repo=https://github.com/yourusername/tamilmv-scraper">
    <img src="https://render.com/images/deploy-to-render-button.svg" width="180">
  </a>
  &nbsp;
  <a href="https://app.koyeb.com/deploy?type=git&repository=github.com/yourusername/tamilmv-scraper&branch=main&name=tamilmv-scraper">
    <img src="https://www.koyeb.com/static/images/deploy/button.svg" width="180">
  </a>
</p>
---

🧩 Example Log

🔍 Fetching TamilMV topics...
📄 Found 12 topics to check.
⬇️ Downloading: ⚡YourBotName⚡ - Bigg Boss Tamil S09 EP08 TRUE WEB-DL.torrent
✅ Uploaded successfully to Telegram
💾 Saved to MongoDB
✅ TamilMV scraping cycle completed.


---

📦 Requirements

Python ≥ 3.10

Pyrogram v2.x

CloudScraper

BeautifulSoup4

Requests

Motor / PyMongo


All dependencies are included in requirements.txt.


---

💬 Credits

👨‍💻 Developed by @SMDxTG 

⚡ Built with Pyrogram

🌍 Content fetched from Private TamilMV sources

🧠 MongoDB powered tracking system



---

<p align="center">
  ⭐ <b>Star this repository</b> if you find it useful!  
  <br>Made with ❤️ for automation & open-source lovers.
</p>
```
