from selenium.webdriver.common.by import By
from functools import wraps

# def find_element(by, value):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(self, *args, **kwargs):
#             # Find the element
#             element = self.driver.find_element(by, value)
#             # Log the screenshot for this element
#             #remove due to duplication
#             #self.screenshot_util.log_screenshot(self.driver, f"Found element {value}", (by, value))
#             # Call the actual function with the element
#             return func(self, element, *args, **kwargs)
#         return wrapper
#     return decorator
from functools import wraps
from selenium.common.exceptions import NoSuchElementException

def find_element(by, value):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            try:
                # Find the element
                element = self.driver.find_element(by, value)
                # Call the actual function with the element
                return func(self, element, *args, **kwargs)
            except NoSuchElementException:
                self.logger.error(f"Element not found: {value}")
                return None  # or raise an exception, depending on your needs
        return wrapper
    return decorator