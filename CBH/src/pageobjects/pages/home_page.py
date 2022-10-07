from CBH.src.pageobjects.locators.home_locators import Locator
from CBH.src.selenimun_extended import SeleniumExtended



class Home_Page():

    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def home_page_loaded(self,driver):
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


