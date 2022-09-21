from CBH.SRC.TestBase.WebdriverSetup import *
from CBH.SRC.PageObject.Pages.Home import *
from selenium.webdriver.common.by import By

#class Homepg(object):
    #def Homepg(driver):
driver=webdriver.Chrome()
Home_Page(driver)
driver.find_elements(By.XPATH, Locator.ham_menu)