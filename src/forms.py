import asyncio
from playwright.async_api import async_playwright
import json

async def fill_contact_form(url, name, email, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        result_data = {
            "tool": "form_tester",
            "url_tested": url,
            "status": "pending",
            "error": None
        }
        
        try:
            await page.goto(url)
            # Professional fallback: wait for any input if specific names aren't found
            await page.wait_for_load_state("networkidle")
            await page.type('input', name, delay=100) 
            result_data["status"] = "Successfully interacted with form"
        except Exception as e:
            result_data["status"] = "Failed"
            result_data["error"] = str(e)
        
        with open("results.json", "w") as f:
            json.dump(result_data, f, indent=4)
            
        await browser.close()
        return result_data["status"]