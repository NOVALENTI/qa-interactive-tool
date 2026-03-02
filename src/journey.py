import asyncio
from playwright.async_api import async_playwright
import json

async def simulate_user_journey(url, search_term):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        journey_log = {
            "tool": "user_journey",
            "start_url": url,
            "search_term": search_term,
            "steps_completed": [],
            "final_status": "Success"
        }
        
        try:
            await page.goto(url)
            journey_log["steps_completed"].append("Landed on Homepage")
            await page.wait_for_load_state("networkidle")
            journey_log["steps_completed"].append(f"Searching for {search_term}")
            
        except Exception as e:
            journey_log["final_status"] = f"Failed: {str(e)}"
        
        with open("results.json", "w") as f:
            json.dump(journey_log, f, indent=4)
        
        await browser.close()
        return journey_log["steps_completed"]