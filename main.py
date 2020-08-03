import requests
from bs4 import BeautifulSoup

target_url = "https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit=50&radius=25"

r = requests.get(target_url)

soup = BeautifulSoup(r.text, "html.parser")

pagination = soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")

spans = []

for page in pages:
    spans.append(page.find("span"))

print(spans[:-1])  