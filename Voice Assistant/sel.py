from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class infow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        search.send_keys(Keys.ENTER)

    def play_video(self, query):
        self.query = query
        self.driver.get(
            f"https://www.youtube.com/results?search_query={self.query}")
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        time.sleep(100)
