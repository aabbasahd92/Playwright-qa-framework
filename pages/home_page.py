from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("#search")
        self.search_button = page.locator("#btn")
        self.result = page.locator("#result")

    def search(self, text: str):
        self.search_input.fill(text)
        self.search_button.click()

    def get_result(self):
        return self.result.text_content()