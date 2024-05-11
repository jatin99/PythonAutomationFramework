from selenium.webdriver.common.by import By


class LoginPage:

    userName = (By.ID, "username")
    password = (By.ID, "password")
    signIn = (By.ID, "submit")
    successMsg = (By.XPATH,"//h1[contains(text(),'Logged In Successfully')]")
    errorMessage =(By.XPATH,"//div[@id='error']")

    def __init__(self, driver):
        self.driver = driver

    def getUserName(self):
        return self.driver.find_element(*LoginPage.userName)

    def getPassWord(self):
        return self.driver.find_element(*LoginPage.password)

    def getSignIn(self):
        return self.driver.find_element(*LoginPage.signIn)

    def getsuccessMsg(self):
        return self.driver.find_element(*LoginPage.successMsg)

    def geterrorMessage(self):
        return self.driver.find_element(*LoginPage.errorMessage)
