from selenium.webdriver.common.by import By


class homepage:
    logOut = (By.XPATH, "//a[contains(text(),'Log out')]")
    workSpace = (By.XPATH, "//a[@id='header-menu']")
    strategicPlan = (By.XPATH,"//a[@title='Strategic Plan']")
    topdownPlan = (By.XPATH,"//a[normalize-space()='Top Down Plan']")
    btmUpPlan = (By.XPATH,"//a[normalize-space()='Bottom-Up Plan']")


    def __init__(self, driver):
        self.driver = driver

    def getlogOut(self):
        return self.driver.find_element(*homepage.logOut)

    def getWorkSpace(self):
        return self.driver.find_element(*homePage.workSpace)

    def getstrategicPlan(self):
        return self.driver.find_element(*homePage.strategicPlan)

    def gettopdownPlan(self):
        return self.driver.find_element(*homePage.topdownPlan)

    def getbtmUpPlan(self):
        return self.driver.find_element(*homePage.btmUpPlan)

