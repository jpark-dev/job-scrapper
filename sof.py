import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://stackoverflow.com/jobs?q=javascript&sort=i&l=Vancouver%2C+BC&d=50&u=Km"


def get_last_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup)


def get_jobs():
    last_page = get_last_page()
    return []
