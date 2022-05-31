from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def text_basket_empty(self):
        empty = self.browser.find_element(*BasePageLocators.BASKED_EMPTY)
        assert 'Your basket is empty.' in empty.text, 'Your basket is not empty'

    def expect_no_products_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKED_ITEMS), 'There are products in the basket'
