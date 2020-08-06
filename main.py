from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs

# indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()

tot_jobs = len(indeed_jobs) + len(sof_jobs)

print(f"Scrapper Done! Scraped {tot_jobs} jobs. Great job, Jason!")