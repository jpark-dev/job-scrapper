from indeed import get_jobs as get_indeed_jobs
from sof import get_jobs as get_sof_jobs

sof_jobs = get_sof_jobs()
indeed_jobs = get_indeed_jobs()

jobs = sof_jobs + indeed_jobs
print(jobs)

print(f"Scrapper Done! Scraped {len(jobs)} jobs. Great job, Jason!")