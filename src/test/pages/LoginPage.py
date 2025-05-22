from utils.wait_for_page import *
from utils.ScreenshotUtil import ScreenshotUtil
from utils.find_element_util import *

class LoginPage:

    @find_element(By.XPATH, '//*[@id="user-name"]')
    def __usernameField(self, usernameField):
        return usernameField

    @find_element(By.XPATH, '//*[@id="password"]')
    def __passwordField(self, passwordField):
        return passwordField

    @find_element(By.XPATH, '//*[@id="login-button"]')
    def __loginButton(self, loginButton):
        return loginButton


    def __init__(self, driver, context, logger):
        self.driver = driver
        self.context = context
        self.logger = logger
        self.screenshot_util = ScreenshotUtil(context)

    def open(self, url):
        self.driver.get(url)

    def enter_credentials(self, username, password):
        wait_for_page_to_load(self.driver,self.__usernameField, retries=2)
        self.__usernameField().send_keys(username)
        self.__passwordField().send_keys(password)
        self.screenshot_util.log_screenshot(self.driver, "Email Input", self.__usernameField, "Username Input")

    def submit_login(self):
        wait_for_page_to_load(self.driver, self.__loginButton, retries=2)
        self.__loginButton().click()

