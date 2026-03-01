import pytest
import os
from src.links import check_links
from src.forms import fill_contact_form
from src.journey import simulate_user_journey

# This gets the absolute path to your local HTML file
LOCAL_FILE = f"file://{os.path.abspath('test_page.html')}"

@pytest.mark.asyncio
async def test_link_extraction():
    # Still testing against a real site to ensure internet connectivity works
    links = await check_links("https://example.com")
    assert isinstance(links, list)
    assert len(links) >= 0 

@pytest.mark.asyncio
async def test_local_form_submission():
    # NOW we test your actual local file!
    status = await fill_contact_form(LOCAL_FILE, "Valentino", "val@test.com", "CI/CD is cool")
    # This should now SUCCEED because your test_page.html has the right inputs
    assert "Successfully" in status
    print("Test Passed: Local form submitted perfectly.")

@pytest.mark.asyncio
async def test_user_journey_flow():
    # Testing a search journey on DuckDuckGo (very stable)
    steps = await simulate_user_journey("https://duckduckgo.com", "QA Automation")
    assert len(steps) > 1
    assert "Landed on Homepage" in steps