import asyncio
from playwright.async_api import async_playwright

async def fill_contact_form(url, name, email, message):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        # We'll use common selectors. If they don't exist, this will fail (as it should in QA!)
        try:
            await page.fill('input[name="name"]', name)
            await page.fill('input[name="email"]', email)
            await page.fill('textarea[name="message"]', message)
            
            # This clicks the submit button
            await page.click('button[type="submit"]')
            
            # Wait for a success message or URL change
            await page.wait_for_load_state("networkidle")
            status = "Submitted Successfully"
        except Exception as e:
            status = f"Form filling failed: {str(e)}"
        
        await browser.close()
        return status
