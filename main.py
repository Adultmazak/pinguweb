from pyrogram import Client, filters
import asyncio
from keep_alive import visit_websites

API_ID = 8249601
API_HASH = "33441ed906e6cf20c47c4c12f67c48cb"
BOT_TOKEN = "7917551868:AAGWHmmK8sRaVlPKL03-iYM2hkOnEVoALxc"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🤖 Bot Activated!\n\nHar 2 min me websites ko visit karega.")

@app.on_message(filters.text)
async def add_website(client, message):
    url = message.text.strip()
    if url.startswith("http://") or url.startswith("https://"):
        with open("websites.txt", "a") as f:
            f.write(url + "\n")
        await message.reply(f"✅ Website Added:\n{url}")
    else:
        await message.reply("❌ Invalid URL. Please send a valid link.")

async def auto_visit():
    while True:
        await visit_websites()
        await asyncio.sleep(120)  # Every 2 minutes

@app.on_message(filters.command("show"))
async def show_websites(client, message):
    try:
        with open("websites.txt", "r") as f:
            sites = f.read()
        await message.reply(f"📄 Websites:\n{sites}")
    except:
        await message.reply("No websites added yet.")

async def main():
    await app.start()
    await auto_visit()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
