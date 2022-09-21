
from selenium import webdriver

class Util:
    def Home_Page(driver):
        driver=webdriver.Chrome()
        driver.get('https://www.amazon.in')
        driver.maximize_window()
        window_before = driver.window_handles[0]


    def total(a, b):
        return a + b
