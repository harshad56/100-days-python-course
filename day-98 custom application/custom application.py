import time

import pyautogui


def custom_automation():

    try:

        # Open a web browser (example using Google Chrome)

        pyautogui.hotkey('winleft')

        pyautogui.write('Google Chrome')

        pyautogui.press('enter')

        time.sleep(2)  # Wait for the browser to open

        # Navigate to a search engine (Google in this example)

        pyautogui.write('https://www.google.com')

        pyautogui.press('enter')

        time.sleep(2)  # Wait for the webpage to load

        # Perform a search

        search_query = 'Custom Automation with Python'

        pyautogui.write(search_query)

        pyautogui.press('enter')

        time.sleep(2)  # Wait for search results

        # Take a screenshot (optional)

        screenshot_path = 'screenshot.png'

        pyautogui.screenshot(screenshot_path)

        print(f"Screenshot saved at: {screenshot_path}")

    except Exception as e:

        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":

    custom_automation()
