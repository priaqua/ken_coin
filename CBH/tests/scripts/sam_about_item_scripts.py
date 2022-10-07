from CBH.src.pageobjects.locators.home_locators import *
from CBH.src.testbase import *
from CBH.src.pageobjects.pages.sam_about_item_page import get_txt_about
from CBH.src.pageobjects.locators.sam_sbout_item_locators import *


def chk_about_txt(self,driver):
    get_txt_about(self,driver)

    if Locator.about_item_txt == "About this item":
        print("Pass- found About this item text on item Samsung TV")
    else:
        print("Test Fail About this item text not found")