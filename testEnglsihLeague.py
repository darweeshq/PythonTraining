import unittest
import kooraPage


class TestStringMethods(unittest.TestCase):
    def __init__(self, browser):
        self.browser = browser

    def test_positive(self):
        firstValue,secondValue = kooraPage.KooraPage.BestPlayersPage(self)
        print('first Value is:'+ firstValue+'| second value is:'+secondValue)
        try:
            assert firstValue == secondValue
            print('Values are equal')
        except:
            print('Values are not equal, this is not the same page')