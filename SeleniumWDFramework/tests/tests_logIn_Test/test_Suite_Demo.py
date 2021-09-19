import unittest
from tests.tests_logIn_Test.test_User_Login import test_UserLogin
from tests.tests_logIn_Test.test_User_login_Csv import test_UserLogin_csv

# get all test from the test class

tc1 = unittest.TestLoader().loadTestsFromTestCase(test_UserLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_UserLogin_csv)

# create a test suite combining all the test classes

functionalLoginTest = unittest.TestSuite([tc1, tc2])

# running the test suite
unittest.TextTestRunner(verbosity=5).run(functionalLoginTest)
