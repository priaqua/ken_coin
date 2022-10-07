from _ast import arguments
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class SeleniumExtended:
    def __init__(self,driver):
        self.driver=driver
        self.timeout=10

    def find_element(self,element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element))

    def wait_click(self,element):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(element)).click(element)

    def scroll_to_element_click_js(self,tuple, element):
        #from _ast import arguments
        #tuple example in this case is
        #tuple_TAE = (By.XPATH, '//*[@id="hmenu-content"]//a[@class="hmenu-item"]')
        #element example
        #element_TAE= driver.find_element(By.XPATH, '//*[@id="hmenu-content"]//a[@class="hmenu-item"]')
        #place tuple and element in Locator file

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(tuple))
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(5)
        element.click()

    def scroll_click_actionchains(self,element):
        # use actionchains
        # this block works
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
