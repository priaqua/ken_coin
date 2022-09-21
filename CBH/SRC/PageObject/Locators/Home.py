### All the locators used in Home page
#locators in here are a Xpath, Class and ID

#menutext              :Class
# ham_menu             :CSS selector
# TV_App_Elect and TV  :Xpath

# Choose better queries
# TV= driver.find_element(By.PARTIAL_LINK_TEXT, 'television')
# //*[@id="hmenu-content"][@text()="Televisions"]

class Locator(object):

        menutext='hm-icon-label'
        ham_menu='#nav-hamburger-menu>span'
        TV_App_Elect='//*[@id="hmenu-content"]/ul[1]/li[16]/a'
        TV='//*[@id="hmenu-content"]/ul[9]/li[3]/a'