from selenium.webdriver.common.by import By


class searchres():

    def __init__(self, driver):
        self.driver = driver

    parent = (By.XPATH, "//div[@class='sg-row']/div[2]/div")

    mobile = (By.XPATH, "//div[@class='sg-row']/div[2]/div/div[1]/div[1]/div/div[1]/h2/a")

    price = (By.XPATH, "//div[@class='sg-row']/div[2]/div/div[2]/div/div/div/div/div/div/a/span[1]")

    def getparent(self):
        return self.driver.find_elements(*searchres.parent)

    def getmobile(self):
        return self.driver.find_elements(*searchres.mobile)

    def getprices(self):
        return self.driver.find_elements(*searchres.price)
