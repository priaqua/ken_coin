import pytest
from selenium import webdriver
import os



#@pytest.fixture(params=("chrome","firefox"),scope="class")
@pytest.fixture(scope="class")
def driver_initiate(request):
    global driver
    supprted_browsers= {"Chrome","Firefox","Edge","Safari","chrome"}
    browser=os.environ.get("Browser")
    if not browser:
        raise Exception ("set Browser in environmental variables")
    browser=browser.lower()
    if browser not in supprted_browsers:
        raise Exception (f"Passed browser {browser} is not in supported browser list.supported browsers are {supprted_browsers} "
                         f"Add the {browser} to the list")
    if browser=="chrome":
        driver = webdriver.Chrome()
    if browser=="Firefox":
        driver= webdriver.Firefox
    # if browser=="Edge":
    #     driver=webdriver.Edge
    # if browser=="Safari":
    #     driver=webdriver.safari
    request.cls.driver=driver
    yield
    driver.quit()