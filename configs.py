import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
USER_SESSION = os.getenv("USER_SESSION", "") # Use Pyrogram V2 String Session 
#if you don't have string Gen bot - use it my bot @SMD_StringBot

# Web
PORT = int(os.getenv("PORT", "8080")) 
URL = os.getenv("URL", "https://rss-tmv-j2i2.onrender.com") # Heroku or Koyeb Or Render Base Url 

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "") #Mongodb Url 
DATABASE_NAME = os.getenv("DATABASE_NAME", "@Nachannel4") # example Cluster0

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.cymru/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", "-1003715942118"))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", "-5118678943"))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", "0"))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://i.ibb.co/Dx8QVdc/file-1799.jpg") #torrant Pic
BOT_TAG = os.getenv("BOT_TAG", "") # File Prefix

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "300"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", "50"))  # Default: 50 GB
