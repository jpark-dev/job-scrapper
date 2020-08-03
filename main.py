import requests
from bs4 import BeautifulSoup

target_url = "https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit=50&radius=25"

r = requests.get(target_url)

soup = BeautifulSoup(r.text, "html.parser")

pagination = soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
pages = []

for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]

print(max_page)