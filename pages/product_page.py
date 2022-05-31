from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basked = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKED)
        basked.click()

    def cost_of_product_coincides_with_basket(self):
        assert self.is_element_present(*ProductPageLocators.COST_OF_BASKED), "Cost of product is not presented"
        assert self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCTS).text == self.browser.find_element(
            *ProductPageLocators.COST_OF_BASKED).text, 'The cost of the basket does not match the price of the product'

    def message_name_coincides_product_name(self):
        assert self.is_element_present(*ProductPageLocators.NAME_BASKED), \
            'There is no message that the product has been added to the cart'
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCTS).text == self.browser.find_element(
            *ProductPageLocators.NAME_BASKED).text, 'The product name in the message does not match the product'
