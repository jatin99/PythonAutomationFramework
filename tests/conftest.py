
from datetime import datetime

import time
import datetime
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service

driver = None
# s = Service("C:\\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
# driver.get('chrome://settings/')


@pytest.fixture(scope="class")
def setup(request):
    global driver
    test = Service()
    driver = webdriver.Chrome(service=test)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the Pytest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace(":", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height=228px;"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%b_%d_%H_%M_%S_%f_%p')
    screenshot_path = st + "_" + "Screenshot.png"
    driver.get_screenshot_as_file('C:\\Dec16\\UIAutomation\\GMG-1\\errorScreenshots' + "\\" + screenshot_path)



