from indeed import extract_pages, extract_jobs

last_indeed_pages = extract_pages()

extract_jobs(last_indeed_pages)


# for n in range(max_page):
#     print(f"start={n * 50}")