import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import TextFeild


class form:
    browser = webdriver.Chrome()
    # def __init__(self,browser):
    #     self.browser = browser
    url = "https://jeronlineforms.jerusalem.muni.il/ConfirmationForStructure"
    browser.get(url)

    testCases_first_name_feild = [
            {"first_name": "דרוויש",  "expected_value": ""},
            {"first_name": " ",  "expected_value": "שדה חובה"},
            {"first_name": "Darweesh", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
            {"first_name": "1234567", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
            {"first_name": "ש", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
            {"first_name": "عربي", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"},
            {"first_name": "דרוויש1", "expected_value": "יש להזין אותיות בעברית בלבד ותווים מיוחדים"}]
    test_data = [
        ("a", "a"),
        ("a", "4"),
        ("6", "9"),
        ("2", "2")
    ]
    @pytest.mark.parametrize("firstn,expected_value",test_data)
    def test_name_cases(self,firstn,expected_value):
          browser = webdriver.Chrome()
          textFieldClass = TextFeild.textFeild
          firstName = textFieldClass(browser,'שם פרטי', firstn)
          lastName = textFieldClass(browser,'שם משפחה','קימרי')
          idNumber = textFieldClass(browser,'מספר ת.ז.','039886544')
          Mobile = textFieldClass(browser,'cellphone','5768719')
          Phone = textFieldClass(browser,'phone','6287296')
          Email = textFieldClass(browser, 'דוא"ל', 'darweeshq@gmail.com')
          actualValue = browser.find_element(By.XPATH, '//div[@class="ng-star-inserted"]').text
        # actualValue = browser.find_element(By.XPATH, '//div[@class="ng-star-inserted"]').text

          assert expected_value == actualValue
