import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

print("First heading on the page:")
print(soup.find("h1").text.strip()) 

print("\nAll product titles (h3 tags):")
for h in soup.find_all("h3"):
    print("-", h.text.strip())

print("\nAll links on the page:")
for a in soup.find_all("a"):
    print("-", a.get_text(strip=True), ":", a.get("href"))
