import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Configurations.Base_class import Basefunc


class AddVendor:
    def __init__(self, driver):
        self.driver = driver

    # Add Vendor Page
    vendor_mod_xpath = "//a[@class='nav-link sub text-uppercase']"
    button_add_new_xpath = '//*[@id="main_nav"]/div/a'
    txt_vendor_name_xpath = "//input[@id='input_vendor_name']"
    drop_dwn_vendor_type_xpath = '//*[@id="input-vendor-type"]'
    txt_first_name_xpath = "//input[@id='input-first-name']"
    # txt_last_name_xpath = "//body/form[@id='vendorForm']/div[@id='content']/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]"
    txt_last_name_xpath = "//input[@placeholder='LAST NAME']"
    txt_vendor_code_xpath = "//body/form[@id='vendorForm']/div[@id='content']/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/input[1]"
    txt_address_xpath = '//*[@id="input-address"]'
    txt_city_xpath = "//*[@id='input-city']"
    txt_state_xpath = "//*[@id='input-state']"
    txt_phone_xpath = "//input[@id='input-phone']"
    txt_zip_xpath = "//input[@id='input-zip']"
    txt_email_xpath = "//input[@id='vemail']"
    drop_dwn_plcb_type_xpath = '//*[@id="content"]/div[2]/div/div/div[5]/div[1]/div[2]/select'
    drop_dwn_edi_xpath = '//*[@id="EDISelector"]'
    button_save_xpath = '//*[@id="form-vendor"]'
    button_cancel_xpath = '//*[@id="main_nav"]/div[2]/a'

    def clickOnVendorMenu(self):
        self.driver.find_element(By.XPATH, self.vendor_mod_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.button_add_new_xpath).click()

    def setVendorName(self, vendorname):
        self.driver.find_element(By.XPATH, self.txt_vendor_name_xpath).send_keys(vendorname)

    def setVendorType(self, value):
        vendor_type_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
        vendor_type_drp.select_by_visible_text(value)

    # def setVendorType(self):
    #     vendor_type_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
    #     vendor_type_drp.select_by_index(2)

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.txt_last_name_xpath).send_keys(lname)

    def setVendorCode(self, vendorcode):
        self.driver.find_element(By.XPATH, self.txt_vendor_code_xpath).send_keys(vendorcode)

    def setAddress(self, address):
        self.driver.find_element(By.XPATH, self.txt_address_xpath).send_keys(address)

    def setCity(self, city):
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)

    def setState(self, state):
        self.driver.find_element(By.XPATH, self.txt_state_xpath).send_keys(state)

    def setphone(self, phone):
        self.driver.find_element(By.XPATH, self.txt_phone_xpath).send_keys(phone)

    def setZip(self, zip):
        self.driver.find_element(By.XPATH, self.txt_zip_xpath).send_keys(zip)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def setPlcb(self, value1):
        plcb_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
        plcb_drp.select_by_visible_text(value1)

    def setEdi(self, value2):
        Edi_drp = Select(self.driver.find_element(By.XPATH, self.drop_dwn_vendor_type_xpath))
        Edi_drp.select_by_visible_text(value2)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()

    def clickOnCancel(self):
        self.driver.find_element(By.XPATH,self.button_cancel_xpath).click()


    def VendorModule(self):
        self.clickOnVendorMenu()
        self.clickOnAddnew()

    def SrchModule(self):
        self.clickOnVendorMenu()

    def AddNewModule(self,vname,fname,lname,vcode,address,city,state,phone,vzip,email):
        self.setVendorName(vname)
        self.setFirstName(fname)
        self.setLastName(lname)
        self.setVendorCode(vcode)
        self.setAddress(address)
        self.setCity(city)
        self.setState(state)
        self.setphone(phone)
        self.setZip(vzip)
        self.setEmail(email)
        # self.setPlcb(plcb)

        self.clickOnSave()
        time.sleep(5)

