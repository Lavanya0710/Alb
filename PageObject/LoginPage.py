from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "input_email"
    textbox_password_id = "input-password"
    button_login_xpath = "//*[@id='card']/div/form/button"
    button_logout_xpath = "/html/body/header/div/div/div/div[3]/ul/li[4]/a/i"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
