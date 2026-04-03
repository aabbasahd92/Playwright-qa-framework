from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    page.goto("http://localhost:8000")
    expect(page).to_have_title("My Test Site")

def test_search_button(page: Page):
    page.goto("http://localhost:8000")
    page.locator("#search").fill("Playwright")
    page.locator("#btn").click()
    expect(page.locator("#result")).to_have_text("You searched: Playwright")