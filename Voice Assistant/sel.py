from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time


class infow:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def get_info(self, query):
        try:
            self.query = query
            self.driver.get("https://www.wikipedia.org")
            search = self.driver.find_element(
                By.XPATH, '//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)
            search.send_keys(Keys.ENTER)
            while True:
                try:
                    # If the title is not accessible, it means the window is closed
                    if self.driver.title == "":
                        self.driver.quit()
                        break
                except WebDriverException:
                    break
                time.sleep(1)
        except NoSuchElementException as e:
            print(f"An error occured: {e}")

    def play_video(self, query):
        try:
            self.query = query
            self.driver.get(
                f"https://www.youtube.com/results?search_query={self.query}")
            video = self.driver.find_element(
                By.XPATH, '//*[@id="video-title"]')
            video.click()
            while True:
                try:
                    # If the title is not accessible, it means the window is closed
                    if self.driver.title == "":
                        self.driver.quit()
                        break
                except WebDriverException:
                    break
                time.sleep(1)
        except NoSuchElementException as e:
            print(f"An error occured: {e}")
        finally:
            self.driver.quit()
