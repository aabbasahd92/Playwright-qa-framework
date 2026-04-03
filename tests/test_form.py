
from playwright.sync_api import Page
from pages.form_page import FormPage

def test_select_country(form):
    form.select_country("ae")
    form.accept_terms()
    form.select_gender("male")
    form.submit_form()
    assert form.get_result() == "Submitted: ae | agreed | male"

def test_missing_country(form):
    form.accept_terms()
    form.select_gender("female")
    form.submit_form()
    assert form.get_result() == "Error: Select a country"

def test_missing_terms(form):
    form.select_country("uk")
    form.select_gender("male")
    form.submit_form()
    assert form.get_result() == "Error: Accept terms"

def test_female_gender(form):
    form.select_country("in")
    form.accept_terms()
    form.select_gender("female")
    form.submit_form()
    assert form.get_result() == "Submitted: in | agreed | female"
