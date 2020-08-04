from indeed import extract_pages, extract_indeed_jobs

last_indeed_pages = extract_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_pages)

print(indeed_jobs)

# for n in range(max_page):
#     print(f"start={n * 50}")