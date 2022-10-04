import time
import webbrowser
from _ast import arguments

from selenium.webdriver.common.by import By
from CBH.src.pageobjects.locators.home_locators import Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def menu_click(self,driver):
    # driver.find_element(By.CSS_SELECTOR, Locator.ham_menu)
    # Locator.ham_menu.click()
    #above two lines are replaced by below
    WebDriverWait(driver,5).until(EC.visibility_of_element_located(Locator.ham_menu)).click(Locator.ham_menu)

def shop_by_cat(self,driver):
    # driver.find_element(By.XPATH, Locator.element_shop_by_cat)
    # driver.execute_script("arguments[0].scrollIntoView(true);",Locator.element_shop_by_cat)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locator.shop_by_cat)).\
        driver.execute_script(arguments[0].scrollIntoView(True), Locator.shop_by_cat)

# Locate scroll and click TV, Appliance, Electranics
def tv_appliance_electronics(self,driver):
    # driver.find_element(By.XPATH, Locator.TV_App_Elect)
    # driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV_App_Elect)
    #time.sleep(5)
    #Locator.TV_App_Elect.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locator.tv_app_elect)).\
        driver.execute_script(arguments[0].scrollIntoView(True), Locator.tv_app_elect)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locator.tv_app_elect)).click(Locator.tv_app_elect)



# Locate and click TV
def television(self,driver):
    # driver.find_element(By.XPATH, Locator.TV)
    # driver.execute_script("arguments[0].scrollIntoView(true);", Locator.TV)
    # #time.sleep(5)
    # Locator.TV.click()

    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locator.tv)).\
        driver.execute_script(arguments[0].scrollIntoView(True), Locator.tv)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locator.tv)).click(Locator.tv)


