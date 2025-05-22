# import os
# from utils.utils import capture_and_highlight_screenshot
#
# class ScreenshotUtil:
#     def __init__(self, context):
#         """
#         Initialize the ScreenshotUtil with the given context.
#         Args:
#             context: Behave context object to store screenshots.
#         """
#         self.context = context
#         if not hasattr(context, 'screenshots'):
#             context.screenshots = []
#
#     # def log_screenshot(self, driver, message, locator=None, description=""):
#     #     """
#     #     Capture and log a screenshot with a message and optional locator for highlighting.
#     #
#     #     Args:
#     #         driver: WebDriver instance.
#     #         message: Descriptive message for the screenshot.
#     #         locator: Locator tuple for highlighting the element (optional).
#     #     """
#     #     # Ensure the `reports/screenshots` folder structure exists
#     #     base_screenshot_path = "reports/screenshots"
#     #
#     #     if description:
#     #         message += f"-{description}"
#     #
#     #     # Capture and highlight the screenshot
#     #     screenshot_path = capture_and_highlight_screenshot(
#     #         driver, base_screenshot_path, message, locator
#     #     )
#     #
#     #     # Avoid duplicate entries by checking if the screenshot already exists in the context
#     #     if screenshot_path and screenshot_path not in [screenshot["path"] for screenshot in self.context.screenshots]:
#     #         self.context.screenshots.append({
#     #             "path": screenshot_path,
#     #             "description": message
#     #         })
#
#     def log_screenshot(self, driver, message, element=None, description=""):
#         """
#         Capture and log a screenshot with a message and optional element for highlighting.
#
#         Args:
#             driver: WebDriver instance.
#             message: Descriptive message for the screenshot.
#             element: WebElement to highlight (optional).
#         """
#         # Ensure the `reports/screenshots` folder structure exists
#         base_screenshot_path = "reports/screenshots"
#         os.makedirs(base_screenshot_path, exist_ok=True)  # Create directory if it doesn't exist
#
#         if description:
#             message += f" - {description}"
#
#         try:
#             # Capture and highlight the screenshot
#             screenshot_path = capture_and_highlight_screenshot(
#                 driver, base_screenshot_path, message, element
#             )
#
#             # Log the screenshot capture
#             if screenshot_path:
#                 self.context.logger.info(f"Screenshot captured: {screenshot_path}")
#             else:
#                 self.context.logger.warning("Screenshot capture failed.")
#
#             # Avoid duplicate entries by checking if the screenshot already exists in the context
#             if screenshot_path and screenshot_path not in [screenshot["path"] for screenshot in
#                                                            self.context.screenshots]:
#                 self.context.screenshots.append({
#                     "path": screenshot_path,
#                     "description": message
#                 })
#         except Exception as e:
#             self.context.logger.error(f"Error capturing screenshot: {e}")
#

import os
from utils.utils import capture_and_highlight_screenshot


class ScreenshotUtil:
    def __init__(self, context):
        """
        Initialize the ScreenshotUtil with the given context.
        Args:
            context: Behave context object to store screenshots.
        """
        self.context = context
        if not hasattr(context, 'screenshots'):
            context.screenshots = []

    def log_screenshot(self, driver, message, element=None, description=""):
        """
        Capture and log a screenshot with a message and optional element for highlighting.

        Args:
            driver: WebDriver instance.
            message: Descriptive message for the screenshot.
            element: WebElement to highlight (optional).
        """
        # Ensure the `reports/screenshots/{scenario_name}` folder exists
        scenario_name = self.context.scenario.name.replace(" ", "_")
        base_screenshot_path = os.path.join("reports", "screenshots", scenario_name)
        os.makedirs(base_screenshot_path, exist_ok=True)

        if description:
            message += f" - {description}"

        try:
            # Capture and highlight the screenshot
            screenshot_path = capture_and_highlight_screenshot(
                driver, base_screenshot_path, message, element
            )

            # Log the screenshot capture
            if screenshot_path:
                self.context.logger.info(f"Screenshot captured: {screenshot_path}")
            else:
                self.context.logger.warning("Screenshot capture failed.")

            # Avoid duplicate entries by checking if the screenshot already exists in the context
            if screenshot_path and screenshot_path not in [s["path"] for s in self.context.screenshots]:
                self.context.screenshots.append({
                    "path": screenshot_path,
                    "description": message
                })
        except Exception as e:
            self.context.logger.error(f"Error capturing screenshot: {e}")