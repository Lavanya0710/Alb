from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basefunc():
    def __init__(self, driver):
        self.driver = driver

    def wait_presence_of_element_located(self, id_type, ele_id):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((id_type, ele_id)))
