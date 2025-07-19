import json, time, threading
import requests
from pyrogram import Client, filters

API_ID = 8249601
API_HASH = "33441ed906e6cf20c47c4c12f67c48cb"
BOT_TOKEN = "7917551868:AAGWHmmK8sRaVlPKL03-iYM2hkOnEVoALxc"

app = Client("keepalive_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

WEBSITE_FILE = "websites.json"

def load_links():
    try:
        with open(WEBSITE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_links(links):
    with open(WEBSITE_FILE, "w") as f:
        json.dump(links, f)

@app.on_message(filters.private & filters.text)
def save_link(client, message):
    link = message.text.strip()
    if link.startswith("http"):
        links = load_links()
        if link not in links:
            links.append(link)
            save_links(links)
            message.reply_text(f"✅ Link saved: {link}")
        else:
            message.reply_text("⚠️ Link already exists.")
    else:
        message.reply_text("❌ Invalid URL.")

def keep_alive():
    while True:
        links = load_links()
        for link in links:
            try:
                requests.get(link, timeout=10)
                print(f"[✓] Visited: {link}")
            except Exception as e:
                print(f"[✗] Failed: {link} — {e}")
        time.sleep(120)

# Start background thread
threading.Thread(target=keep_alive, daemon=True).start()

# Start bot
app.run()
