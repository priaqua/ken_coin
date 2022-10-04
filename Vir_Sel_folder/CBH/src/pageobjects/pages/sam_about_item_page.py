from selenium.webdriver.common.by import By
from CBH.src.pageobjects.locators.sam_sbout_item_locators import *



def get_txt_about(self,driver):
    driver.find_element(By.XPATH,Locator.about_item_txt)