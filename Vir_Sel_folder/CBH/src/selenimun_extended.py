from _ast import arguments
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtended:
    def __init__(self,driver):
        self.driver=driver
        self.timeout=timeout

    def click(self,element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element)).click(element)
