from selenium.webdriver.common.by import By
from CBH.src.pageobjects.pages.home_page import *
from CBH.conftest import *


# from CBH.driver_config import *

def home_page(driver):
    driver.get('https://www.amazon.in')
    driver.maximize_window()
    window_before = driver.window_handles[0]
    assert driver.find_element(By.CLASS_NAME, 'hm-icon-label'), "Cannot find Menu on Home Page"
def clickmenu(driver):
    menu_click(driver)
    tv_appliance_electronics(driver)
    television(driver)
    assert driver.find_element(By.XPATH,
                               '//*[@id="nav-search-label-id"][text()="Televisions"]'), "Television page did not load"


