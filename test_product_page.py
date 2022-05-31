import pytest
import time

from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email=str(time.time()) + "@fakemail.org", password='qwerty228')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.message_name_coincides_product_name()
        page.cost_of_product_coincides_with_basket()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
        page = ProductPage(browser, link)
        page.open()
        assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'element present'

        
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    links = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, links)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_name_coincides_product_name()
    page.cost_of_product_coincides_with_basket()
    

@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket2(browser, link):
    links = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, links)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.message_name_coincides_product_name()
    page.cost_of_product_coincides_with_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.expect_no_products_in_basket()
    page.text_basket_empty()
