import http.client

conn = http.client.HTTPSConnection("linkedin-data-scraper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "9010927403msh1000be5f814482fp19f61ajsn0b7f36144b09",
    'x-rapidapi-host': "linkedin-data-scraper.p.rapidapi.com"
}

conn.request("GET", "/company_insights?link=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Fgoogle", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))