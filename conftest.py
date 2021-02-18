import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")



@pytest.fixture(scope="class")
def browserinvo(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="D:\\chromedriver")


    elif browser == "firefox" or browser == "IE":
        print("Browser is not supported")

    request.cls.driver = driver
    yield
    driver.close()




