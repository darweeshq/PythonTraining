from selenium import webdriver
import kooraPage
import testEnglsihLeague

class mianPage:
    browser = webdriver.Chrome()
    Koora = kooraPage.KooraPage(browser)
    Koora.load()
    Koora.clickOnMain()
    testEnglsihLeague.TestStringMethods(browser).test_positive()
    Koora.scrolldown()
    Koora.scrollup()

