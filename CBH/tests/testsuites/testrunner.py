# import self as self
import pytest
from CBH.conftest import *
from CBH.config_url import *
from CBH.src.pageobjects.pages.home_page import Home_Page
from CBH.src.selenimun_extended import *


@pytest.mark.usefixtures("driver_initiate")
class Test:
    def test_homepage(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        home_page=Home_Page(self)
        assert home_page.home_page_loaded(self), "Home page did not load"
        home_page.menu_click(self)
        home_page.scroll_select_tv_appliance_electronics(self.driver)
        home_page.scroll_select_television(self.driver)
        assert home_page.assert_TV_displayed(self.driver), "Television page did not load"
