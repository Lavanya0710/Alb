import time
import pytest
from selenium.webdriver.common.by import By

from PageObject.AddVendor import AddVendor
from PageObject.LoginPage import LoginPage
from PageObject.searchVendorPage import SearchVendor
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig


class Test_SearchVendorName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchVendorName(self,setup):
        self.logger.info("************* Search_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search vendor **********")

        self.addvendor = AddVendor(self.driver)
        self.addvendor.clickOnVendorMenu()

        self.logger.info("************* searching the Vendor **********")

        sv = SearchVendor(self.driver)
        sv.setVendorName('laddu123')
        sv.clickCheckBox()
        time.sleep(1)
        time.sleep(5)
        self.driver.close()

        self.logger.info("***************  TC_ByName_005 Finished  *********** ")