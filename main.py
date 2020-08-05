from indeed import extract_pages, extract_indeed_jobs

last_indeed_pages = extract_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_pages)


print(indeed_jobs)
print()
print(f"Scrapper Done! Scraped {len(indeed_jobs)} jobs. Great job, Jason!")