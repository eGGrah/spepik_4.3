from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKED = (By.CSS_SELECTOR, '[class="btn-group"]')
    BASKED_EMPTY = (By.CSS_SELECTOR, '[id="content_inner"]')
    BASKED_ITEMS = (By.CSS_SELECTOR, '[class="basket-title hidden-xs"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REG_EMAIL = (By.CSS_SELECTOR, '[id="register_form"] [type="email"]')
    REG_PASSWORD = (By.CSS_SELECTOR, '[id="register_form"] [name="registration-password1"]')
    REG_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[id="register_form"] [name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKED = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    COST_OF_PRODUCTS = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > [class="price_color"]')
    COST_OF_BASKED = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"]  strong')
    NAME_BASKED = (
        By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-success  fade in"] [class="alertinner "] strong')
    NAME_PRODUCTS = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
