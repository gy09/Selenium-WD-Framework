import unittest
from page.Page_logIn_Test.page_User_Login import Login_Page
from utilities.teststatus import TestStatus
import time
import pytest
from utilities.readData import getCSVData
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class test_UserLogin_csv(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.LP = Login_Page(self.driver)
        self.TS = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    @data(*getCSVData('C:\\Users\\Lenovo\\workspace_python\\SeleniumWDFramework\\utilities\\dataFile.csv'))
    @unpack
    def test_User_Login_Success(self, username, password):
        self.LP.login_page(username, password)
        result1 = self.LP.verifypageTitle()
        self.TS.mark(result1, "The title doesn't match the expected title")

        result2 = self.LP.verifyLoginSuccess()
        self.TS.markFinal(testName="test_User_Login_Success", result=result2, resultMessage="The login failed")

    @pytest.mark.run(order=1)
    def test_User_Login_Failed(self):
        self.LP.login_page("gaurav03y@gmail.com", "XXXXXX")
        result = self.LP.verifyLoginFailed()
        time.sleep(10)
        assert result == True


if __name__ == '__main__':
    unittest.main()
