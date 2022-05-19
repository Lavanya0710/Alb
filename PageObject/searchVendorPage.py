from selenium.webdriver.common.by import By


class SearchVendor():
    # Add Vendor Page
    txt_SupplierCode_id = "supplier_code"
    txtVendorName_id = "vendor_name"
    txtPhoneNo_id = "phone"
    txtEmail_id = "email"
    # CheckBox_xpath = "//tr[1][starts-with(@id,'vendor-row')]//child::td[1]"
    CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    Delete_xpath = "//button[@id='vender_delete']"


    # tblSearchResults_xpath='//*[@id="vendor"]/tbody'
    # table_xpath='//*[@id="form-vendor"]/div'
    # tableRows_xpath='//*[@id="vendor-row"]'
    # tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSupplierCode(self, code):
        self.driver.find_element(By.ID, self.txt_SupplierCode_id).clear()
        self.driver.find_element(By.ID, self.txt_SupplierCode_id).send_keys(code)

    def setVendorName(self, vname):
        self.driver.find_element(By.ID, self.txtVendorName_id).clear()
        self.driver.find_element(By.ID, self.txtVendorName_id).send_keys(vname)

    def setPhone(self, number):
        self.driver.find_element(By.ID, self.txtPhoneNo_id).clear()
        self.driver.find_element(By.ID, self.txtPhoneNo_id).send_keys(number)

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def clickCheckBox(self):
        self.driver.find_element(By.XPATH, self.CheckBox_xpath).click()

    def clickDelete(self):
        self.driver.find_element(By.XPATH, self.Delete_xpath).click()

    # def getNoOfRows(self):
    #     return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
    #
    # def getNoOfColumns(self):
    #     return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))
    #
    # def searchCustomerByEmail(self,email):
    #     flag=False
    #     for r in range(1,self.getNoOfRows()+1):
    #       table=self.driver.find_element_by_xpath(self.table_xpath)
    #       emailid=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
    #       if emailid == email:
    #           flag = True
    #           break
    #     return flag
    #
    # def searchCustomerByName(self,Name):
    #     flag=False
    #     for r in range(1,self.getNoOfRows()+1):
    #       table=self.driver.find_element_by_xpath(self.table_xpath)
    #       name=table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
    #       if name == Name:
    #           flag = True
    #           break
    #     return flag
