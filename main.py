from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from contextlib import contextmanager
from selenium.webdriver.common.by import By
import os
import subprocess

load_dotenv(".env")


class Bot:

    @contextmanager
    def wait_for_page_load(self, xpath=None, selector=None, timeout=60):
        try:
            if xpath is not None:
                yield WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            elif selector is not None:
                yield WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                )
            else:
                raise Exception("Xpath and select are both empty")
        except NoSuchElementException:
            print("No such element")

    @contextmanager
    def wait_for_page_clickable(self, xpath=None, selector=None, timeout=60):
        try:
            if xpath is not None:
                yield WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elif selector is not None:
                yield WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
            else:
                raise Exception("Xpath and select are both empty")
        except NoSuchElementException:
            print("No such element")

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, options=chrome_options)

    def checkout_google_button(self):
        self.driver.get("https://www.google.com.hk")

        with self.wait_for_page_load(
                xpath="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input") as input_field:
            input_field.send_keys("hello")

            # find button by text
            with self.wait_for_page_clickable(xpath="//*[contains(text(), 'Privacy')]") as search_button:
                search_button.click()


if __name__ == '__main__':

    # kill all chrome first
    if os.name == "nt":
        subprocess.call("taskkill /IM chrome.exe")
    elif os.name == "posix":
        os.system("pkill -9 Google Chrome")

    bot = Bot()

    bot.checkout_google_button()
