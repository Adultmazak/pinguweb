import threading
import time
import requests
from pyrogram import Client

urls = [
    "https://example1.com",
    "https://example2.com",
    "https://example3.com"
]

def auto_ping():
    while True:
        for url in urls:
            try:
                r = requests.get(url)
                print(f"[✓] Visited: {url} | Status: {r.status_code}")
            except Exception as e:
                print(f"[x] Error visiting {url}: {e}")
        time.sleep(120)

api_id = 8249601      # <-- yahan apna API_ID daalo
api_hash = "33441ed906e6cf20c47c4c12f67c48cb"  # <-- yahan apna API_HASH daalo
bot_token = "7917551868:AAGWHmmK8sRaVlPKL03-iYM2hkOnEVoALxc"  # <-- yahan apna BOT_TOKEN daalo

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
def reply(client, message):
    message.reply_text("✅ Bot is online and pinging websites!")

threading.Thread(target=auto_ping).start()

app.run()
