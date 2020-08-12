import requests
from bs4 import BeautifulSoup

LIMIT = 50
# URL = f"https://stackoverflow.com/jobs?q=javascript&sort=i&l=Vancouver%2C+BC&d=50&u=Km"
URL = f"https://stackoverflow.com/jobs?q=javascript&sort=i&l=Canada"


def get_last_page():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

def extract_job(html):
    title = html.find("h2", {"class":"fs-body3"}).find("a")["title"]
    company, location = html.find("h3", {"class":"fs-body1"}).find_all("span", recursive=False)
    # print(title, company.get_text(strip=True), location.get_text(strip=True))
    job_id = html['data-jobid']
    return {'title':title, 'company': company.get_text(strip=True), 'location': location.get_text(strip=True), 'apply_link': f"https://stackoverflow.com/jobs?id={job_id}"}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"======== Scrapping from Stack Overflow: PG: {page+1} ========")
        r = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(r.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
