from playwright.sync_api import sync_playwright, BrowserContext

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://revamp-amadeus.beyonderissolutions.com/auth/login")  # Replace with actual login URL

        # Case 1: Valid Login
        page.fill('input[name="email"]', 'usamaadmin@mail.com')
        page.fill('input[name="password"]', '1234')
        page.click('button[type="submit"]')
        browser_context = BrowserContext()
        page.wait_for_timeout(7000)  # wait for page to load

        # # Case 2: Invalid Login
        # page.goto("https://revamp-amadeus.beyonderissolutions.com/auth/login")
        # page.fill('input[name="email"]', 'wrong@example.com')
        # page.fill('input[name="password"]', 'wrongpass')
        # page.click('button[type="submit"]')
        # assert page.locator("text=Invalid email or password").is_visible()
        # page.wait_for_timeout(7000) 


        # # Case 3: Empty Fields
        # page.goto("https://revamp-amadeus.beyonderissolutions.com/auth/login")
        # page.click('button[type="submit"]')
        # assert page.locator("text=Email is required").is_visible()
        # assert page.locator("text=Password is required").is_visible()
        # page.wait_for_timeout(7000) 

        browser.close()

test_login()