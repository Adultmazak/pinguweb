import httpx

async def visit_websites():
    try:
        with open("websites.txt", "r") as f:
            urls = f.read().splitlines()
        for url in urls:
            try:
                async with httpx.AsyncClient() as client:
                    await client.get(url, timeout=10)
                print(f"✅ Visited: {url}")
            except Exception as e:
                print(f"❌ Failed to visit: {url} | {e}")
    except FileNotFoundError:
        print("No websites.txt found.")
