
from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Locators.Home import *


def menu_text(self,driver):
    driver.find_element(By.CLASS_NAME, Locator.ham_menu)

