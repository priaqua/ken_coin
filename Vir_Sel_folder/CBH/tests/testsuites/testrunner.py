import pytest
# import self as self
import time
from CBH.tests.scripts.home_scripts import *
from CBH.tests.scripts.television_scripts import *
from CBH.tests.scripts.sam_about_item_scripts import *
from CBH.conftest import *


# from pytest_selenium import *

@pytest.mark.usefixtures("driver_initiate")
class Test():
    def test_amazon(self):
        self.driver.get("https://google.com")

# def amazon(driver):
#     home_page(driver)
#     clickmenu(driver)
#     brand_selection(self, driver)
#     chk_about_txt(self, driver)
