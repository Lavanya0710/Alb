import ddt
import pytest
import time

import softest
from ddt import ddt,data,unpack
from selenium.webdriver.common.by import By

from PageObject.AddVendor import AddVendor
from PageObject.LoginPage import LoginPage
from utilities.customlogger import LogGen
from utilities.readproperties import ReadConfig
from utilities.xlread import Utilities


@ddt
class Test_003_AddVendor(softest.TestCase):
    baseURL = ReadConfig.getApplicationURL()
    #baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    def test_Add_New(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.logger.info("******* Login Object Created Successfully **********")
        self.an = AddVendor(self.driver)
        # print("Add vendor created Successfully")
        self.logger.info("******* Add vendor created Successfully **********")
        self.logger.info("******* Starting Add Vendor Test **********")

    @data(*Utilities.read_data_from_excel('C:\\Users\\getma\\PycharmProjects\\Alb\\TestData\\AddVendor.xlsx','AddNew'))
    @unpack
    def test_Add(self,vname, fname, lname, vcode, address, city, state, phone, vzip, email, plcb):
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.an.Add_New(vname, fname, lname, vcode, address, city, state, phone, vzip, email, plcb)
            # self.an.Add_New(vname, fname, lname, vcode, address, city, state, phone, vzip, email, plcb)
            # self.logger.info("************* Login successful **********")

            self.logger.info("********* Add Vendor validation started *****************")
            try:
              self.msg = self.driver.find_element(By.XPATH,"/html/body/section/div[1]").text
              print(self.msg)
              if 'Vendor created successfully' in self.msg:
                assert True
                self.logger.info("********* Add Vendor Test Passed *********")
                self.driver.close()
                self.logger.info("******* Ending Add Vendor test **********")
            except:
                self.logger.info("********* Already existing vendor *********")
            #     print("Already existing vendor")
            #     self.driver.close()
            #     assert True



