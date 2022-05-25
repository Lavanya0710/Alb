from selenium.webdriver.common.by import By
from Configurations.Base_class import Basefunc

class DeleteVendor(Basefunc):
    Delete_xpath = "//button[@id='vender_delete']"
    CheckBox_xpath = "//tr[starts-with(@id,'vendor-row')]//child::td"
    nomatch_xpath = '//*[@id="vendor"]/tbody/tr/td'
    txtVendorName_id = "vendor_name"
    txtVendorResult_xpath = "//td[@class='text-left'][2]/a"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    def click_CheckBox(self):
        self.wait_presence_of_element_located(By.XPATH, self.CheckBox_xpath).click()

    def clickDelete(self):
        self.wait_presence_of_element_located(By.XPATH, self.Delete_xpath).click()

    def setVendorName(self, vname):
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).clear()
        self.wait_presence_of_element_located(By.ID, self.txtVendorName_id).send_keys(vname)


    def validate(self,vname):
        self.setVendorName(vname)
        name_result = self.wait_presence_of_element_located(By.XPATH, self.txtVendorResult_xpath)
        try:
            if self.setVendorName(vname) == name_result.get_attribute('value'):

                print(name_result.get_attribute('value'))
                self.click_CheckBox()
                self.clickDelete()
            else:
                print('Value not found')
        except:
            print('value not found')

            #     self.get_searchdept().send_keys(d_name)
            #
            # def display_d_name_exist(self, d_name):
            #     print(d_name)
            #     print(self.disp_result().get_attribute("value"))
            #     if d_name in self.disp_result().get_attribute("value"):
            #         print("------------------------------------------")
            #         print(self.disp_result().get_attribute("value"))
            #     else:
            #         print("**------------********")
            #         print('Value Does Not Exist')


