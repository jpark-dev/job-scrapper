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

def extract_job(html):
    title = html.find("h2", {"class":"title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    company_anchor = company.find("a")
    
    if company_anchor is not None:
        target_text = company_anchor
    else:
        target_text = company

    company = str(target_text.string).strip()

    location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]

    return {
        'title': title, 
        'company': company, 
        'location': location,
        'link': f"https://ca.indeed.com/viewjob?jk={job_id}" 
        }

def extract_indeed_jobs(last_page):
    jobs = []

    # for page in range(last_page):
    # r = requests.get(f"{URL}&start={page*LIMIT}")
    r = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(r.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs
