import cfscrape
from bs4 import BeautifulSoup

# Use cfscrape to get site data (due to Cloudflare's anti-bot measures) and then BeautifulSoup to parse the HTML
scraper = cfscrape.create_scraper()
catalogue = BeautifulSoup(scraper.get('https://www.corwoodindustries.com').text, 'html.parser')

records = []
cost = 0

# Count the number of asterisks after each record title
for title in catalogue.find_all('a'):
    if title.get_text().startswith('0'):
        records.append(title.get_text().count('*'))

# Correlate the number of asterisks to the legend and update the total cost accordingly
for record in records:
    if record == 5:
        cost += 27
    elif record == 4:
        cost += 34
    elif record == 3:
        cost += 22
    elif record == 2:
        cost += 18
    elif record == 1:
        cost += 18
    else:
        cost += 10

# 50% discount on 20 or more releases
cost = str(cost / 2)
if cost.endswith('.5'):
    cost = f'{cost}0'

print(f"The complete Jandek discography currently costs ${cost} USD when ordered directly from Corwood Industries.")
