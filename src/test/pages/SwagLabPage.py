from utils.wait_for_page import *
from utils.ScreenshotUtil import ScreenshotUtil
from utils.find_element_util import *

class SwagLabPage:

    @find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    def __addProduct(self, addProduct):
        return addProduct

    @find_element(By.XPATH, '//*[@id="shopping_cart_container"]')
    def __cartButton(self, cartButton):
        return cartButton

    @find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
    def __productInCart(self, productInCart):
        return productInCart

    @find_element(By.XPATH, '//div[text()="Swag Labs"]')
    def __swagLabsText(self, swagLabsText):
        return swagLabsText

    @find_element(By.XPATH, '//button[text()="Remove"]')
    def __removeProduct(self, removeProduct):
        return removeProduct

    @find_element(By.XPATH, '//button[text()="Checkout"]')
    def __checkoutButton(self, checkoutButton):
        return checkoutButton


    def __init__(self, driver, context, logger):
        self.driver = driver
        self.context = context
        self.logger = logger
        self.screenshot_util = ScreenshotUtil(context)

    def swag_dashboard(self):
        wait_for_page_to_load(self.driver, self.__swagLabsText, retries=2)
        assert self.__swagLabsText().is_displayed(), "Element is not visible"

    def add_product_to_cart(self):
        wait_for_page_to_load(self.driver, self.__addProduct, retries=2)
        self.__addProduct().click()
        self.screenshot_util.log_screenshot(self.driver, "Product List", self.__addProduct, "Product List")
        self.__cartButton().click()
        self.screenshot_util.log_screenshot(self.driver, "Product Added to Cart", self.__cartButton,
                                            "Product Added to Cart")

    def product_added_to_cart(self):
        assert self.__productInCart().is_displayed(), "Element is not visible"
        self.screenshot_util.log_screenshot(self.driver, "Product Added to Cart", self.__productInCart,
                                            "Product Added to Cart")

    def delete_product_to_cart(self):
        wait_for_page_to_load(self.driver, self.__addProduct, retries=2)
        self.__addProduct().click()
        self.screenshot_util.log_screenshot(self.driver, "Product List", self.__addProduct, "Product List")
        self.__cartButton().click()
        self.screenshot_util.log_screenshot(self.driver, "Product Remove to Cart", self.__removeProduct,
                                            "Product Remove to Cart")
        self.__removeProduct().click()

    def product_delete_to_cart(self):
        assert self.__checkoutButton().is_displayed(), "Element is not visible"
        self.screenshot_util.log_screenshot(self.driver, "Product Remove to Cart", self.__checkoutButton,
                                            "Product Remove to Cart")
