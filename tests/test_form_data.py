import json
import pytest
from playwright.sync_api import Page
from pages.form_page import FormPage

with open("test-data/form_data.json") as f:
    data = json.load(f)

@pytest.mark.parametrize("case", data["valid_submissions"])
def test_valid_submission(form, case):
    form.select_country(case["country"])
    form.accept_terms()
    form.select_gender(case["gender"])
    form.submit_form()
    assert form.get_result() == case["expected"]

@pytest.mark.parametrize("case", data["invalid_submissions"])
def test_invalid_submission(form, case):
    if case["country"]:
        form.select_country(case["country"])
    if case["terms"]:
        form.accept_terms()
    if case["gender"]:
        form.select_gender(case["gender"])
    form.submit_form()
    assert form.get_result() == case["expected"]
