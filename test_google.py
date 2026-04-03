from playwright.sync_api import Page, expect

def test_google_title(page: Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_google_search(page: Page):
    page.goto("https://www.google.com")
    page.locator("textarea[name='q']").fill("Playwright Python")
    page.keyboard.press("Enter")
    import re
    expect(page).to_have_url(re.compile("search"))