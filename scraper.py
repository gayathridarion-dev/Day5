from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_songs_from_youtube(query):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    search_url = f"https://www.youtube.com/results?search_query={query}"
    driver.get(search_url)

    time.sleep(3)

    videos = driver.find_elements(By.ID, "video-title")

    results = []
    for video in videos[:5]:
        title = video.get_attribute("title")
        link = video.get_attribute("href")
        results.append({"title": title, "link": link})

    driver.quit()
    return results