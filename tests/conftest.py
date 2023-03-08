import os

import pytest
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--URL", action="store", default="https://rahulshettyacademy.com/angularpractice/"
    )


# @pytest.fixture(scope="class")
@pytest.fixture()
def setup(request):
    global driver

    url = request.config.getoption("URL")
    browser_name = request.config.getoption("browser_name")
    match browser_name:
        case "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
            print("<<<-------------------- CHROME BROWSER WAS STARTED -------------------->>>")
        case "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            print("<<<-------------------- EDGE BROWSER WAS STARTED -------------------->>>")
        case _:
            raise ValueError("<<<Browser type value is incorrect!>>>")

    driver.implicitly_wait(3)
    driver.maximize_window()
    # driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get(url)

    request.cls.driver = driver
    yield
    attach(
        driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG
    )
    print("<<<-------------------- "
          + os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
          + " was finished -------------------->>>")
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
