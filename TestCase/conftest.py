import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
    return driver
#
# @pytest.fixture()
# def setup(browser):
#     if browser =='chrome':
#         driver=webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))
#         print("Launching chrome browser.........")
#     elif browser=='firefox':
#         driver=webdriver.Firefox(service=Service(geckodriver_autoinstaller.install()))
#         print("Launching firefox browser.........")
#     return driver
#
# def pytest_addoption(parser):    # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")



# -----------------------------PyTest HTML REPORT-------------------------------------------
def pytest_configure(config):
    config._metadata['Project Name'] = 'Alberta'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Lavanya'

@pytest.mark.optionhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)