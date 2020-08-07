import requests
from bs4 import BeautifulSoup

LIMIT = 50
# URL = f"https://stackoverflow.com/jobs?q=javascript&sort=i&l=Vancouver%2C+BC&d=50&u=Km"
URL = f"https://stackoverflow.com/jobs?q=javascript&sort=i"


def get_last_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        r = requests.get(f"{URL}&pg={page+1}")
        print(r.status_code)
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            print(result["data-jobid"])


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
