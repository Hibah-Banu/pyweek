from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

URL = "https://www.imdb.com/chart/top/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
time.sleep(2)

# Collect movie rows
rows = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")

data = []

for row in rows[:10]:   # Scrape first 20 movies (you can increase)
    title = row.find_element(By.CSS_SELECTOR, ".ipc-title__text").text
    year = row.find_element(By.CSS_SELECTOR, ".cli-title-metadata-item").text
    rating = row.find_element(By.CSS_SELECTOR, ".ipc-rating-star--rating").text

    print(f"{title} → {year} → {rating}")

    data.append({
        "Title": title,
        "Year": year,
        "Rating": rating
    })


pd.DataFrame(data).to_csv("imdb_top_movies.csv", index=False)

print("\nScraping complete! Data saved to imdb_top_movies.csv")

driver.quit()


