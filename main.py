from re import search

from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver")
driver.get("https://www.amazon.in/")

driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Samsung Mobiles")
driver.find_element_by_id("nav-search-submit-button").click()
parentmob = driver.find_elements_by_xpath("//div[@class='sg-row']/div[2]/div")
mobil = []
price = []

for parent in parentmob:
    mobiles =parent.find_elements_by_xpath("div[1]/div[1]/div/div[1]/h2/a")
    prices = parent.find_elements_by_xpath("div[2]/div/div/div/div/div/div/a/span[1]")
    for mobile, pric in zip(mobiles, prices):

        if search("Samsung", mobile.text):
            str = mobile.text
            spltstr = str.split("(")
            mobil.append(spltstr[0])
            price.append(pric.text)

for i, j in zip(mobil, price):
    print(i, j)












#//div[@class='sg-row']/div[2]/div

#//div[@class='sg-row']/div[2]/div/div[1]/div[1]/div/div[1]/h2/a - Mobile
#//div[@class='sg-row']/div[2]/div/div[2]/div/div/div/div/div/div/a/span[1] - Price