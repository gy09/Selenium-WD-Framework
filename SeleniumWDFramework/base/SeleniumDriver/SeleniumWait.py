from selenium.webdriver.common.by import By
from Selenium_Driver import Selenium_Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import *
from traceback import print_stack


class ExplicitWaitType():

    def __init__(self, driver):
        self.driver = driver
        self.SD = Selenium_Driver(driver)

    def waitForElement(self, timeout, poll_Frequency, locatorType, locator):

        element = None
        try:
            byType = self.SD.getByType(locatorType)

            wait = WebDriverWait(self.driver, timeout=timeout, poll_Frequency=poll_Frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(Ec.visibility_of_element_located(byType, locator))

            print("Element is located ")
        except:
            print("Element to be located not found")
            print_stack()
        return element 
