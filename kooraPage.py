import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class KooraPage:
    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get("https://www.kooora.com/")
        time.sleep(4)

    def clickOnMain(self):
        time.sleep(4)
        clickOnMain = self.browser.find_element(By.XPATH, "(//a[@class='nav_li_link'])[1]")
        clickOnMain.click()

    def BestPlayersPage(self):
        time.sleep(4)
        clickOnMain = self.browser.find_element(By.XPATH, "(//a[@class='nav_li_link'])[5]")
        clickOnMain.click()
        time.sleep(4)
        EnglishLeague = self.browser.find_element(By.XPATH, "(//a[@class='match_league'])[1]")

        EnglishLeagueMenuName = EnglishLeague.text


        EnglishLeague.click()
        time.sleep(4)
        Title = self.browser.title
        print('from class the title is:' + Title)
        return Title , EnglishLeagueMenuName

    def scrolldown(self):
        scrolldown = self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(1)

    def scrollup(self):
        scrollup = self.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.HOME)
        time.sleep(1)





