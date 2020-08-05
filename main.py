from indeed import get_jobs as get_indeed_jobs

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)

print(f"Scrapper Done! Scraped {len(indeed_jobs)} jobs. Great job, Jason!")