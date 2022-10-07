
from selenium.webdriver.common.by import By
### All the locators used in Home page
#locators in here are a Xpath, Class and ID

#menutext              :Class
# ham_menu             :CSS selector
# TV_App_Elect and TV  :Xpath

# Choose better queries
# TV= driver.find_element(By.PARTIAL_LINK_TEXT, 'television')
# //*[@id="hmenu-content"][@text()="Televisions"]

class Locator(object):

        #assertiont for Home page loaded
        assert_menutext = (By.CLASS_NAME,'hm-icon-label')

        # locators for navigation on Home page
        Hamburger_Menu = (By.CSS_SELECTOR, '#nav-hamburger-menu>span')
        Shop_By_Category = (By.XPATH, '//*[contains(@class,"hmenu-title")][text()="shop by category"]')
        TV_Apppliance_Electronics = (By.XPATH, '//*[@id="hmenu-content"]//a[@class="hmenu-item"]//div[contains(text(),"TV, Appliances, Electronics")]')
        TV=(By.XPATH, '*//a[@class="hmenu-item"][contains(text(),"Televisions")]')

        #Locator for assertion -Television page loaded
        assert_TV_page = (By.XPATH, '//*[@id="nav-search-label-id"][text()="Televisions"]')
