import time
import pytest
from PageObjects.LoginPage import LoginPage
from PageObjects.homepage import homepage
from utilities.BaseClass import baseclass
from testdata.login import login



class Test_Case1(baseclass):
    def test_casedemo1(self, getDataLogin):
        log = self.getLogger()
        log.info("Test case 1: Positive LogIn test")
        login = LoginPage(self.driver)
        log.info("UserNavigated to login page")
        login.getUserName().send_keys(getDataLogin["UserName"])
        login.getPassWord().send_keys(getDataLogin["PassWord"])
        login.getSignIn().click()
        self.assert_url(getDataLogin["expected_Url"])
        log.info("Verfified Url")
        actual_SuccssMsg= login.getsuccessMsg().text
        assert actual_SuccssMsg=="Logged In Successfully", "SuccessMessage Mismatch"
        log.info("Verify button Log out is displayed on the new page")
        homePage = homepage(self.driver)
        assert homePage.getlogOut().is_displayed(),"LogOut Button not displayed"
        homePage.getlogOut().click()
        log.info("Verified button Log out is displayed on the new page")
        log.info("TestCase 1 Executed Successfully")


    def test_casedemo2(self, getDataLogin):
        log = self.getLogger()
        log.info("Test case 2: Negative username test")
        login = LoginPage(self.driver)
        log.info("Verify error message is displayed")
        login.getUserName().send_keys(getDataLogin["InValidUserName"])
        login.getPassWord().send_keys(getDataLogin["InValidPassWord"])
        login.getSignIn().click()
        self.waitTillElementshown(login.errorMessage)
        log.info("Verified error message is displayed")
        actual_ErrorMsg = login.geterrorMessage().text
        assert actual_ErrorMsg == "Your username is invalid!", "Error Message Mismatch"
        log.info("Test case 2: Negative username test Executed Successfully")





    @pytest.fixture(params=login.test_login_data)
    def getDataLogin(self, request):
        return request.param