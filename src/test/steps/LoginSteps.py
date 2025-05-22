from behave import given, when, then
from utils.config import get_base_url
from utils.code_extractor import generate_auth_code
from environments.test.pages.LoginPage import LoginPage
import json
import time


# Load credentials from the credentials.json file
def load_credentials():
    with open('data/credentials.json', 'r') as file:
        credentials = json.load(file)
    return credentials['username'], credentials['password']

def invalid_load_credentials():
    with open('data/invalid_credentials.json', 'r') as file:
        credentials = json.load(file)
    return credentials['username'], credentials['password']

@given('I am on the Swag Labs login page')
def step_impl(context):
    # Load credentials and base URL
    username, password = load_credentials()
    url = get_base_url('swagLabs')

    # Create an instance of the login page and open it
    context.login_page = LoginPage(context.driver, context, context.logger)  # Pass both context.driver and context

    context.login_page.open(url)

    # Screenshot will be automatically taken within the page-level code (quoting_page.py)

@when('I enter valid credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context, context.logger)

    # Load credentials
    username, password = load_credentials()
    context.login_page.enter_credentials(username, password)

    # Screenshot will be automatically taken within the page-level code (quoting_page.py)

@when('I submit the login form')
def step_impl(context):
    context.login_page = LoginPage(context.driver, context, context.logger)
    context.login_page.submit_login()
