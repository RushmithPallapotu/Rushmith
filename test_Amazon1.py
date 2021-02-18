from re import search

import pytest
from selenium import webdriver

from PageObjects.Homepage import Homepage
from PageObjects.Searchresults import searchres
from TestData.testdata import testdata
from Utilties.Utilties import Baseclass


class TestAmazon(Baseclass):


    def test_get_mobiles_prices(self, getdata):

        log = self.loggerinfo()

        self.driver.get("https://www.amazon.in/")

        hopg =  Homepage(self.driver)
        seres = searchres(self.driver)

        hopg.getsearchbox().send_keys(getdata["Item"])
        log.info(getdata["Item"]+"is entered")
        hopg.getsearchbut().click()

        parentmob = seres.getparent()
        mob       = seres.getmobile()
        pricc     = seres.getprices()

        mobil = []
        price = []

        for mobile, pric in zip(mob, pricc):

            if search(getdata["Search"], mobile.text):
                str = mobile.text
                spltstr = str.split("(")
                mobil.append(spltstr[0])
                price.append(pric.text)

        log.info("All items are captured")
        for i, j in zip(mobil, price):
            log.info(print(i, j))

    @pytest.fixture(params=testdata.testdatamz)
    def getdata(self, request):
        return request.param


