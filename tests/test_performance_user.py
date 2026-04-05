import pytest
import time
from playwright.sync_api import Page
from pages.performance_page import PerformancePage

STANDARD_USER = "standard_user"
PERFORMANCE_USER = "performance_glitch_user"
PROBLEM_USER = "problem_user"

def test_standard_user_login_time(page: Page):
    perf = PerformancePage(page)
    duration = perf.login_and_measure(STANDARD_USER)
    assert duration < 5.0, f"Standard login too slow: {duration:.2f}s"
    print(f"Standard user login: {duration:.2f}s")

def test_performance_user_login_time(page: Page):
    perf = PerformancePage(page)
    duration = perf.login_and_measure(PERFORMANCE_USER)
    assert duration < 15.0, f"Performance user login too slow: {duration:.2f}s"
    print(f"Performance user login: {duration:.2f}s")

def test_performance_vs_standard_comparison(page: Page):
    perf = PerformancePage(page)
    standard_time = perf.login_and_measure(STANDARD_USER)
    page.goto("https://www.saucedemo.com")
    perf2 = PerformancePage(page)
    performance_time = perf2.login_and_measure(PERFORMANCE_USER)
    print(f"Standard: {standard_time:.2f}s | Performance: {performance_time:.2f}s")
    assert performance_time > standard_time, "Performance user should be slower than standard"

def test_sort_az_standard_user(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(STANDARD_USER)
    perf.sort_and_measure("az")
    names = perf.get_product_names()
    assert names == sorted(names), "Products not sorted A-Z"

def test_sort_za_standard_user(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(STANDARD_USER)
    perf.sort_and_measure("za")
    names = perf.get_product_names()
    assert names == sorted(names, reverse=True), "Products not sorted Z-A"

def test_sort_price_low_high(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(STANDARD_USER)
    perf.sort_and_measure("lohi")
    prices = perf.get_product_prices()
    assert prices == sorted(prices), "Prices not sorted low to high"

def test_sort_price_high_low(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(STANDARD_USER)
    perf.sort_and_measure("hilo")
    prices = perf.get_product_prices()
    assert prices == sorted(prices, reverse=True), "Prices not sorted high to low"

def test_problem_user_sort_az(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(PROBLEM_USER)
    perf.sort_and_measure("az")
    names = perf.get_product_names()
    is_sorted = names == sorted(names)
    print(f"Problem user A-Z sort correct: {is_sorted}")
    print(f"Names: {names}")

def test_problem_user_product_count(page: Page):
    perf = PerformancePage(page)
    perf.login_and_measure(PROBLEM_USER)
    count = perf.get_product_count()
    assert count == 6, f"Expected 6 products but got {count}"

def test_all_users_see_6_products(page: Page):
    users = [STANDARD_USER, PERFORMANCE_USER, PROBLEM_USER]
    for user in users:
        perf = PerformancePage(page)
        perf.login_and_measure(user)
        count = perf.get_product_count()
        assert count == 6, f"{user} sees {count} products instead of 6"
        page.goto("https://www.saucedemo.com")