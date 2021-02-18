from selenium.webdriver.common.by import By


class Homepage():

    def __init__(self, driver):
        self.driver = driver

    searchbox = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    searchbut = (By.ID, "nav-search-submit-button")

    def getsearchbox(self):
        return self.driver.find_element(*Homepage.searchbox)

    def getsearchbut(self):
        return self.driver.find_element(*Homepage.searchbut)
