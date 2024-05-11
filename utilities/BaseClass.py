import inspect
import logging

from datetime import datetime

import time
import datetime

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver


@pytest.mark.usefixtures("setup")
class baseclass:
    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def verifylinkpresence(self, text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(text))

    def assert_url(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {self.driver.current_url}"

    def verifyelementclickable(self, xpaths):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.element_to_be_clickable(xpaths))

    def waitTillElementshown(self, xpaths):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located(xpaths))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def getactionsdoubleclick(self, xpath):
        action= ActionChains(self.driver)
        action.double_click(xpath).perform()

    def getrightclick(self, xpath):
        action= ActionChains(self.driver)
        action.context_click(xpath).perform()

    def gethoweronelement(self, xpath):
        action = ActionChains(self.driver)
        action.move_to_element(xpath).perform()

    def verifytextpresence(self, linkText):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(linkText))

    def getscrolltoview(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get80resolution(self):
        self.driver.execute_script("document.body.style.zoom='80%'")

    def get60resolution(self):
        self.driver.execute_script("document.body.style.zoom='60%'")

    def getRefreshbrowser(self):
        self.driver.refresh()

    def getimplicitwait(self):
        self.driver.implicitly_wait(30)

    def getswitchtoFrame(self, xpath):
        self.driver.switch_to.frame(xpath)

    def getSwitchToDefaultContent(self):
        self.driver.switch_to.default_content()

    def get100resolution(self):
        self.driver.execute_script("document.body.style.zoom='100%'")

    def get60resolution(self):
        self.driver.execute_script("document.body.style.zoom='60%'")

    def getclick(self, Xpath):
        self.driver.execute_script("arguments[0].click();", Xpath)

    def getRightScroll(self, Xpath):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", Xpath)

    def getrightArrow(self):
        self.driver.send_keys(Keys.ARROW_RIGHT)

    def getCatpureScreen(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%b_%d_%H_%M_%S_%f_%p')
        screenshot_path = st + "_" + "Screenshot.png"
        self.driver.save_screenshot('C:\\Dec16\\UIAutomation\\FastRetail\\Screenshots' + "\\" + screenshot_path)

    def getDismissPopup(self):
        self.driver.switch_to.default_content

    def getPageSource(self, listname):
        test = self.driver.page_source
        print(test)
        a = len(listname)
        n = a - 1
        x = 0
        while 0<=x<=n:
            if (listname[x] in test):
                print(listname[x])
                print("order is present in the webpage")
            else:
                print(listname[x])
                print("order is not present in the webpage")

            x = x+1





