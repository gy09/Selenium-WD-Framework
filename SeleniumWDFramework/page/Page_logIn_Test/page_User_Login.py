from selenium.webdriver.common.by import By
import time
from base.SeleniumDriver.Selenium_Driver import Selenium_Driver
from base.SeleniumDriver.basepage import BasePage


class Login_Page(BasePage):

    # the below method takes the driver instance in the constructor and initiate it

    def __init__(self, driver):
        # we are creating driver instance for the inherited class
        super().__init__(driver)
        self.driver = driver

    # Locators
    __loginLink = "//a[@href = '/login']"
    __emailTextBox = "//input[@id= 'email']"
    __passwordTextBox = "//input[@id ='password']"
    __logInBtn = "//input[@class ='btn btn-default btn-block btn-md dynamic-button']"

    # Below method are to identify the web element
    # def get_loginLink(self):
    #     return self.driver.find_element(By.XPATH, self.__loginLink)
    #
    # def get_emailTextBox(self):
    #     return self.driver.find_element(By.XPATH, self.__emailTextBox)
    #
    # def get_passwordTextBox(self):
    #     return self.driver.find_element(By.XPATH, self.__passwordTextBox)
    #
    # def get_logInBtn(self):
    #     return self.driver.find_element(By.XPATH, self.__logInBtn)

    # Below method are action method which will work on the web Element

    def click_loginLink(self):
        self.element_Click("xpath", self.__loginLink)

    def send_emailTextBox(self, username):
        self.element_Sendkeys(username, "xpath", self.__emailTextBox)

    def send_passwordTextBox(self, password):
        self.element_Sendkeys(password, "xpath", self.__passwordTextBox)

    def click_logInBtn(self):
        self.element_Click("xpath", self.__logInBtn)

    def login_page(self, username, password):
        self.click_loginLink()
        self.send_emailTextBox(username)
        self.send_passwordTextBox(password)
        self.click_logInBtn()

    def verifyLoginSuccess(self):
        result = self.get_elementIsPresent("xpath", "//a[contains(@class,'navbar-brand navbar-logo text-blue')]")
        return result

    def verifyLoginFailed(self):
        result = self.get_elementIsPresent("xpath", "//span[contains(text(),'Your username or password is invalid. "
                                                    "Please try again.')]")
        return result

    def verifyEmptyLoginField(self):
        result = self.get_elementIsPresent("xpath", "")

        return result

    def verifypageTitle(self):
        return self.verifyPageTitle("My Courses")  # My Courses
