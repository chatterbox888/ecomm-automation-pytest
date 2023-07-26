
from demostore_automation.src.selenium_extended.SeleniumExtended import SeleniumExtended
from demostore_automation.src.pages.locators.OrderReceivedPageLocators import OrderReceivedPageLocators

import time

class OrderReceivedPage(OrderReceivedPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_contains_text(self.PAGE_MAIN_HEADER, "Order received")

    time.sleep(3)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)

    time.sleep(3)

