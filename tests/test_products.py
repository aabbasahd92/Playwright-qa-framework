import json
import pytest
from pages.products_page import ProductsPage

with open("test-data/products_data.json") as f:
    data = json.load(f)

def test_products_page_loads(products):
    assert products.get_product_count() == 6

def test_default_sort_is_az(products):
    names = products.get_product_names()
    assert names == sorted(names)

def test_sort_name_az(products):
    products.sort_by("az")
    names = products.get_product_names()
    assert names == sorted(names)

def test_sort_name_za(products):
    products.sort_by("za")
    names = products.get_product_names()
    assert names == sorted(names, reverse=True)

def test_sort_price_low_to_high(products):
    products.sort_by("lohi")
    prices = products.get_product_prices()
    assert prices == sorted(prices)

def test_sort_price_high_to_low(products):
    products.sort_by("hilo")
    prices = products.get_product_prices()
    assert prices == sorted(prices, reverse=True)

def test_all_products_have_names(products):
    names = products.get_product_names()
    assert all(len(name) > 0 for name in names)

def test_all_products_have_prices(products):
    prices = products.get_product_prices()
    assert all(price > 0 for price in prices)

def test_add_single_item_to_cart(products):
    products.add_product_to_cart(0)
    assert products.get_cart_count() == 1

def test_add_multiple_items_to_cart(products):
    products.add_product_to_cart(0)
    products.add_product_to_cart(1)
    products.add_product_to_cart(2)
    assert products.get_cart_count() == 3
