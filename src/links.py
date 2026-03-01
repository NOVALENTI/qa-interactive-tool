import asyncio
from playwright.async_api import async_playwright

async def check_links(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        # Find all link elements
        links = await page.query_selector_all('a')
        results = []

        for link in links:
            href = await link.get_attribute('href')
            if href and href.startswith('http'):
                # We'll just collect them for now
                results.append(href)
        
        await browser.close()
        return results

# This allows you to run it manually to test
if __name__ == "__main__":
    found_links = asyncio.run(check_links("https://example.com"))
    print(f"Found {len(found_links)} links!")
