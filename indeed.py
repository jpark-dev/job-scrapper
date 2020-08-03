import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit={LIMIT}&radius=25"

def extract_pages():
    r = requests.get(URL)

    soup = BeautifulSoup(r.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

def extract_jobs(last_page):
    for page in range(last_page):
        print(f"&start={page*LIMIT}")
