import asyncio
import argparse
import sys
import os
from src.links import check_links
from src.forms import fill_contact_form
from src.journey import simulate_user_journey

async def run_manual_menu():
    print("\n--- QA INTERACTIVE TOOLBOX (MANUAL MODE) ---")
    print("1. Link Validator")
    print("2. Form Tester")
    print("3. User Journey Simulator")
    
    choice = input("\nSelect a tool (1-3): ")

    if choice == "1":
        url = input("Enter URL to check: ")
        print(f"Running Link Validator on {url}...")
        await check_links(url)
        print("Success! Results saved to results.json")
    
    elif choice == "2":
        url = input("Enter URL with form: ")
        print(f"Running Form Tester on {url}...")
        await fill_contact_form(url, "QA_Bot", "bot@test.com", "Automated Test")
        print("Success! Results saved to results.json")

    elif choice == "3":
        url = input("Enter URL to start journey: ")
        term = input("Search term: ")
        print(f"Running Journey Simulator for '{term}'...")
        await simulate_user_journey(url, term)
        print("Success! Results saved to results.json")

async def main():
    parser = argparse.ArgumentParser(description="QA Universal Interactive Toolbox")
    parser.add_argument("--tool", choices=["links", "form", "journey"], help="The tool to run")
    parser.add_argument("--url", help="The target URL")
    parser.add_argument("--term", help="Search term (for journey tool only)")
    
    args = parser.parse_args()

    # If no arguments, go to manual menu
    if len(sys.argv) == 1:
        await run_manual_menu()
        return

    # Automation Logic (The Universal Bridge)
    if args.tool == "links" and args.url:
        await check_links(args.url)
        print(f"Automation Success: Links for {args.url} saved to results.json")
    
    elif args.tool == "form" and args.url:
        await fill_contact_form(args.url, "Bot", "bot@test.com", "Auto-test")
        print(f"Automation Success: Form test for {args.url} saved to results.json")

    elif args.tool == "journey" and args.url and args.term:
        await simulate_user_journey(args.url, args.term)
        print(f"Automation Success: Journey for {args.term} saved to results.json")
    else:
        print("Error: Missing required arguments. Use --help for info.")

if __name__ == "__main__":
    asyncio.run(main())