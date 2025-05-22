from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def wait_for_page_to_load(driver, element_method, timeout=10, retries=3, delay_before_wait=0):
    """Wait for a specific element (from a decorated function) to be visible before continuing."""
    attempt = 0

    if delay_before_wait > 0:
        print(f"Waiting {delay_before_wait} seconds before checking for element...")
        time.sleep(delay_before_wait)

    while attempt < retries:
        try:
            element = element_method()  # ✅ Call the method to get the actual WebElement

            #scroll element into view before waiting for visibility
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

            WebDriverWait(driver, timeout).until(EC.visibility_of(element))
            print(f"✅ Element {element_method.__name__} is now visible.")
            return True  # Exit if successful

        except Exception as e:
            attempt += 1
            print(f"⚠️ Attempt {attempt}/{retries}: Element not found. Retrying in 2 seconds...")

            if attempt == retries:
                print(f"❌ Failed to find element after {retries} attempts: {e}")
                raise  # Raise error after exhausting retries

            time.sleep(5)  # Wait before retrying
