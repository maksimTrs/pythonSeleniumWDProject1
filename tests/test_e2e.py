import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.CheckOutPage import CheckOutPage
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutpage.go_to_checkout_page()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirmpage.set_country_field("india")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        # self.driver.find_element_by_link_text("India").click()
        confirmpage.get_country_name()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()
        confirmpage.submit_purchase_with_checkbox()
        # textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        textMatch = confirmpage.get_purchase_result()
        log.info("Text received from application is " + textMatch)

        assert ("Success! Thank you!" in textMatch)
