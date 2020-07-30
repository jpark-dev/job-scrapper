import requests

target_url = "https://ca.indeed.com/jobs?q=Junior+Developer+-senior%2C+-sr&l=Vancouver%2C+BC&limit=50&radius=25"

r = requests.get(target_url)

print(r)
print(r.text)