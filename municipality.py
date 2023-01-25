import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationForStructurePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure"
        self.first_name_label = 'שם פרטי'
        self.first_name_locator = {
            'By': By.XPATH,
            'Value': f"//label[contains(text(),'{self.first_name_label}')]/following-sibling::input"
        }

    def visit(self):
        self.driver.get(self.url)
        self.first_name_field = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((self.first_name_locator['By'], self.first_name_locator['Value'])))

    def fill_form(self, first_name):
        self.first_name_field.send_keys(first_name)

    def get_first_name_value(self):
        return self.first_name_field.get_attribute('value')


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    driver.quit()


def test_form_submission(driver):
    confirmation_page = ConfirmationForStructurePage(driver)
    confirmation_page.visit()
    confirmation_page.fill_form("John")

    # check that the form was submitted successfully
    assert "John" in confirmation_page.get_first_name_value()

    # add a screenshot to the Allure report
    allure.attach("screenshot", driver.get_screenshot_as_png(), AttachmentType.PNG)
