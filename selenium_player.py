# selenium_player.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def play_song_on_youtube(song_name):
    """Open YouTube and play the first search result"""
    # Set up Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        # Open YouTube
        driver.get("https://www.youtube.com")
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys(song_name + Keys.RETURN)

        # Wait for search results to load
        time.sleep(3)

        # Click the first video
        first_video = driver.find_element(By.ID, "video-title")
        first_video.click()

        # Let video play for a bit
        time.sleep(10)

    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()