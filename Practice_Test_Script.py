from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without opening the browser
        page = browser.new_page()

        # Open Google
        page.goto("https://www.google.com")

        # Print page title
        print("Page title is:", page.title())



# Run the script
run()
