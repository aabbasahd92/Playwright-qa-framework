import time
from playwright.sync_api import Page

class PerformancePage:
    def __init__(self, page: Page):
        self.page = page

    def login_and_measure(self, username: str, password: str = "secret_sauce"):
        start = time.time()
        self.page.goto("https://www.saucedemo.com")
        self.page.fill("[data-test='username']", username)
        self.page.fill("[data-test='password']", password)
        self.page.click("[data-test='login-button']")
        self.page.wait_for_url("**/inventory.html")
        self.page.wait_for_load_state("domcontentloaded")
        duration = time.time() - start
        return duration

    def sort_and_measure(self, option: str):
        start = time.time()
        self.page.locator("[data-test='product-sort-container']").select_option(option)
        self.page.wait_for_load_state("domcontentloaded")
        duration = time.time() - start
        return duration

    def get_product_names(self):
        return self.page.locator("[data-test='inventory-item-name']").all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator("[data-test='inventory-item-price']").all_text_contents()
        return [float(p.replace("$", "")) for p in prices]

    def get_product_count(self):
        return self.page.locator("[data-test='inventory-item']").count()