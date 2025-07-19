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

api_id = 123456       # <-- yahan apna API_ID daalo
api_hash = "your_api_hash"  # <-- yahan apna API_HASH daalo
bot_token = "your_bot_token"  # <-- yahan apna BOT_TOKEN daalo

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
def reply(client, message):
    message.reply_text("✅ Bot is online and pinging websites!")

threading.Thread(target=auto_ping).start()

app.run()
