from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.common.exceptions import *
from traceback import print_stack
from utilities.customLogger import customlogger
import logging
import os
import time


class Selenium_Driver():
    log = customlogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # Method to send the locator type

    def getByType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'tag_name':
            return By.TAG_NAME
        elif locatorType == 'class_name':
            return By.CLASS_NAME
        elif locatorType == 'link_text':
            return By.LINK_TEXT
        elif locatorType == 'partial_link_text':
            return By.PARTIAL_LINK_TEXT
        elif locatorType == 'css_selector':
            return By.CSS_SELECTOR
        elif locatorType == 'xpath':
            return By.XPATH
        else:
            self.log.info("The locator type" + locatorType + "is not a valid locator type")

    # Custom Find Element method

    def getElement(self, locatorType, locator):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found for " + byType + "locator type and " + locator + "locator")

        except:
            self.log.info("Element not found for " + byType + "locator type and " + locator + "locator")
        return element

    # Custom check element is present method

    def get_elementIsPresent(self, locatorType, locator):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorType, locator)

            if element is not None:
                self.log.info("Element is present")
                return True
            else:
                return False
        except:
            self.log.info("Element was not found")
            return False

    # custom element click method

    def element_Click(self, locatorType, locator):

        try:
            element = self.getElement(locatorType, locator)
            element.click()
            self.log.info(
                "The element to be click with Locator Type:" + locatorType + " and locator as :" + locator + "is "
                                                                                                             "clicked")
        except:

            print_stack()

            self.log.info("Element not found")

    # custom send keys method

    def element_Sendkeys(self, data, locatorType, locator):

        try:
            element = self.getElement(locatorType, locator)
            element.send_keys(data)
            self.log.info(
                "The element to be click with Locator Type:" + locatorType + " and locator as :" + locator + "is "
                                                                                                             "clicked")
        except:

            print_stack()

            self.log.info("Element not found")

    # Custom Explicit wait method

    def waitForElement(self, timeout, poll_Frequency, locatorType, locator):

        element = None
        try:
            byType = self.getByType(locatorType)

            wait = WebDriverWait(self.driver, timeout=timeout, poll_Frequency=poll_Frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(Ec.visibility_of_element_located(byType, locator))

            self.log.info("Element is located ")
        except:
            self.log.info("Element to be located not found")
            print_stack()
        return element

    def get_page_Title(self):
        return self.driver.title

    def get_screenshot(self, resultMessage):

        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "..\\..\\screenShots"
        relativeFileName = screenshotDirectory + filename
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screen shot is saved to" + destinationFile + "location")
        except:
            self.log.error("Exception Occurred")
            print_stack()

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")