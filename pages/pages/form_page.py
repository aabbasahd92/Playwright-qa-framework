
from playwright.sync_api import Page

class FormPage:
    def __init__(self, page: Page):
        self.page = page
        self.country = page.locator("#country")
        self.terms = page.locator("#terms")
        self.male = page.locator("#male")
        self.female = page.locator("#female")
        self.upload = page.locator("#upload")
        self.submit = page.locator("#submit-btn")
        self.result = page.locator("#form-result")

    def select_country(self, value: str):
        self.country.select_option(value)

    def accept_terms(self):
        self.terms.check()

    def select_gender(self, gender: str):
        if gender == "male":
            self.male.check()
        else:
            self.female.check()

    def upload_file(self, path: str):
        self.upload.set_input_files(path)

    def submit_form(self):
        self.submit.click()

    def get_result(self):
        return self.result.text_content()
