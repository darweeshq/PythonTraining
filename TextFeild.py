import time
from selenium.webdriver.common.by import By

class textFeild:
    def __init__(self,browser,label,testValue):
        self.browser = browser
        self.label = label
        self.testValue = testValue
        self.setPath()
        self.setPathById()
        self.fillFeild()

    def setPath(self):
        self.textFeild_locator = f"//label[contains(text(),'{self.label}')]/following-sibling::input"

    def setPathById(self):
        self.numberFeild_locator = f"{self.label}"

    def getPath(self):
        return self.textFeild_locator

    def getPathById(self):
        return self.numberFeild_locator

    def fillFeild(self):
        browser = self.browser
        try:
            feild = browser.find_element(By.XPATH, self.getPath())
            browser.find_element(By.XPATH, self.getPath()).clear()

        except:
            time.sleep(.1)
            feild = browser.find_element(By.ID, self.getPathById())

        feild.send_keys(self.testValue)
        time.sleep(.1)