# import self as self
import pytest
from CBH.conftest import *
from CBH.config_url import *

# @pytest.mark.usefixtures("driver_initiate")
# class Test:
#     def test_amazon(self,driver):
#         driver=self.driver
#         driver=webdriver.Chrome()
#         driver.get(URL)

#This works
# @pytest.mark.usefixtures("driver_initiate")
# class Test:
#     def test_amazon(self):
#         self.driver.get(URL)

import pytest
from CBH.src.pageobjects.locators.home_locators import Locator
from CBH.src.selenimun_extended import SeleniumExtended
from CBH.config_url import URL
from selenium import webdriver


class TestHome_Page():

    def test_setup_(self,driver):
        self.driver=driver
        driver=webdriver.Chrome()
        self.driver.get(URL)
        self.driver.maximize_window()
        self.sl=SeleniumExtended(self.driver)

    def test_home_page_loaded(self,driver):
        self.sl.find_element(Locator.assert_menutext)

    def menu_click(self,driver):
        self.sl.wait_click(Locator.Hamburger_Menu)

        # Locate scroll and click TV, Appliance, Electranics
    def scroll_select_tv_appliance_electronics(self,driver):
        self.sl.scroll_click_actionchains(Locator.TV_Apppliance_Electronics)

    # Locate and click TV
    def scroll_select_television(self,driver):
        self.sl.scroll_click_actionchains(Locator.TV)

    def assert_TV_displayed(self,driver):
        self.sl.find_element(Locator.assert_TV_page)





