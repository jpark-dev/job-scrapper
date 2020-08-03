import requests
from bs4 import BeautifulSoup

INDEED_URL = "https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit=50&radius=25"

def extract_pages():
    r = requests.get(INDEED_URL)

    soup = BeautifulSoup(r.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page