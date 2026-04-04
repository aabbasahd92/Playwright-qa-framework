
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.form_page import FormPage
from pages.products_page import ProductsPage

@pytest.fixture
def home(page: Page):
    page.goto("http://localhost:8000/index.html", wait_until="load")
    return HomePage(page)

@pytest.fixture
def form(page: Page):
    page.goto("http://localhost:8000/index.html", wait_until="load")
    return FormPage(page)

@pytest.fixture
def products(page: Page):
    products_page = ProductsPage(page)
    products_page.goto()
    return products_page
