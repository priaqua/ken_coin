import pytest
from selenium.webdriver.common.by import By
from CBH.SRC.PageObject.Pages.extra import *
from CBH.SRC.TestBase.WebdriverSetup import *
from selenium import webdriver


class Testcase:

    @pytest.fixture
    def test_setup(self):
        return 1

    def test_case(self):
        driver=webdriver.Chrome()
        Home_Page(self)
        driver.find_elements(By.XPATH, Locator.ham_menu)