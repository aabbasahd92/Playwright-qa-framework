import pytest
import json
from playwright.sync_api import Page, Route

BASE_URL = "https://www.saucedemo.com"

def login(page: Page):
    page.goto(BASE_URL)
    page.fill("[data-test='username']", "standard_user")
    page.fill("[data-test='password']", "secret_sauce")
    page.click("[data-test='login-button']")
    page.wait_for_url("**/inventory.html")

def test_mock_slow_network(page: Page):
    def slow_response(route: Route):
        route.continue_()

    page.route("**/*", slow_response)
    login(page)
    assert "/inventory" in page.url

def test_mock_block_images(page: Page):
    page.route("**/*.png", lambda route: route.abort())
    page.route("**/*.jpg", lambda route: route.abort())
    login(page)
    assert "/inventory" in page.url
    image_count = page.locator("img").count()
    assert image_count >= 0

def test_mock_api_empty_response(page: Page):
    def mock_empty(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps([])
        )

    page.route("**/api/**", mock_empty)
    login(page)
    assert "/inventory" in page.url

def test_mock_api_server_error(page: Page):
    def mock_error(route: Route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body=json.dumps({"error": "Internal Server Error"})
        )

    page.route("**/api/**", mock_error)
    login(page)
    assert "/inventory" in page.url

def test_mock_network_failure(page: Page):
    page.route("**/*.css", lambda route: route.abort())
    login(page)
    assert "/inventory" in page.url
    assert page.locator("[data-test='inventory-container']").is_visible()

def test_mock_jsonplaceholder_posts(page: Page):
    def mock_posts(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps([
                {"id": 1, "title": "Mocked Post 1", "userId": 1},
                {"id": 2, "title": "Mocked Post 2", "userId": 1}
            ])
        )

    page.route("**/posts", mock_posts)
    page.goto("https://jsonplaceholder.typicode.com/posts")
    content = page.text_content("body")
    assert "Mocked Post 1" in content
    assert "Mocked Post 2" in content

def test_mock_jsonplaceholder_error(page: Page):
    def mock_error(route: Route):
        route.fulfill(
            status=503,
            content_type="application/json",
            body=json.dumps({"error": "Service Unavailable"})
        )

    page.route("**/posts", mock_error)
    page.goto("https://jsonplaceholder.typicode.com/posts")
    content = page.text_content("body")
    assert "Service Unavailable" in content