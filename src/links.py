import asyncio
from playwright.async_api import async_playwright
import json

async def check_links(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        links = await page.eval_on_selector_all("a[href]", "elements => elements.map(el => el.href)")
        
        results = {
            "tool": "link_validator",
            "url_tested": url,
            "total_links": len(links),
            "links": links
        }
        
        with open("results.json", "w") as f:
            json.dump(results, f, indent=4)
            
        await browser.close()
        return links