import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import TextFeild


class TestCalculate:
    browser = webdriver.Chrome()
    url = "https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure"
    browser.get(url)

    testCases_first_name_feild = [
        {"first_name": "דרוויש", "expected_value": ""},
        {"first_name": " ", "expected_value": "שדה חובה"},
        {"first_name": "Darweesh", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
        {"first_name": "1234567", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
        {"first_name": "ש", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
        {"first_name": "عربي", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
        {"first_name": "דרוויש1", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"}]
    # @pytest.fixture
    # def setValue(self,first_name):
    #     self.testvalue = self.testCases_first_name_feild[0][f'"{first_name}"']
    #     return self.testvalue

    @pytest.mark.parametrize("first_name,expected_value",testCases_first_name_feild)
    # I have a problem in here, method fills the key instead of the value !!!!
    def test_calculate(self, first_name, expected_value):
        # maybe = self.testvalue
        textFieldClass = TextFeild.textFeild
        firstName = textFieldClass(self.browser, 'שם פרטי', first_name)
        lastName = textFieldClass(self.browser, 'שם משפחה', 'קימרי')
        idNumber = textFieldClass(self.browser, 'מספר ת.ז.', '039886544')
        Mobile = textFieldClass(self.browser, 'cellphone', '5768719')
        Phone = textFieldClass(self.browser, 'phone', '6287296')
        Email = textFieldClass(self.browser, 'דוא"ל', 'darweeshq@gmail.com')
        actualValue = self.browser.find_element(By.XPATH, '//div[@class="ng-star-inserted"]').text
        # actualValue = browser.find_element(By.XPATH, '//div[@class="ng-star-inserted"]').text
        assert expected_value == actualValue
