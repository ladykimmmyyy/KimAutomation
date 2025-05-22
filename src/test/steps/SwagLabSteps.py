from behave import given, when, then
from utils.config import get_base_url
from utils.code_extractor import generate_auth_code
from environments.test.pages.SwagLabPage import SwagLabPage
import json
import time


# Load credentials from the credentials.json file

@given('I am on the Swag Labs Dashboard')
def step_impl(context):
    context.swagLab_page = SwagLabPage(context.driver, context, context.logger)
    context.swagLab_page.swag_dashboard()

@when('I add a product to cart')
def step_impl(context):
    context.swagLab_page = SwagLabPage(context.driver, context, context.logger)
    context.swagLab_page.add_product_to_cart()

@then('I verify if product is successfully added on the cart')
def step_impl(context):
    context.swagLab_page = SwagLabPage(context.driver, context, context.logger)
    context.swagLab_page.product_added_to_cart()

@when('I delete a product to cart')
def step_impl(context):
    context.swagLab_page = SwagLabPage(context.driver, context, context.logger)
    context.swagLab_page.delete_product_to_cart()

@then('I verify if product is successfully deleted on the cart')
def step_impl(context):
    context.swagLab_page = SwagLabPage(context.driver, context, context.logger)
    context.swagLab_page.product_delete_to_cart()
