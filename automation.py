from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def play_song_on_youtube(song_name):
    # Configure Chrome WebDriver (make sure chromedriver is in PATH)
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(song_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)
    
    # Click the first video
    first_video = driver.find_element(By.ID, "video-title")
    first_video.click()