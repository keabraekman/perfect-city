import sys
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook

workbook = load_workbook('perfect-city.xlsx')
worksheet = workbook.active

states = ["Alaska", "Alabama", "Arkansas", "Arizona", 
"California", "Colorado", "Connecticut", "District-of-Columbia", 
"Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", 
"Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", 
"Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", 
"Montana", "North-Carolina", "North-Dakota", "Nebraska", "New-Hampshire", 
"New-Jersey", "New-Mexico", "Nevada", "New-York", "Ohio", "Oklahoma", 
"Oregon", "Pennsylvania", "Rhode Island", "South-Carolina", 
"South-Dakota", "Tennessee", "Texas", "Utah", "Virginia", 
"Vermont", "Washington", "Wisconsin", "West-Virginia", "Wyoming"]

def get_html(url):
    re = requests.get(url)
    return BeautifulSoup(re.text, 'html.parser')

for s in states:
    target_url = 'https://www.city-data.com/city/' + s + '.html'
    # print(target_url)


soup = get_html('https://www.city-data.com/city/Alaska.html')
tags = soup.tbody

rows = soup.find_all('tr', {'class': 'rB'})
# print(rows[0].find_all('td')[1].b.a.contents[0])


def get_cities(state):
    soup = get_html('https://www.city-data.com/city/' + state + '.html')
    cities = []
    for c in soup.find_all('tr', {'class': 'rB'}):
        cities.append(c.find_all('td')[1].find_all('a')[0].contents[0])
    return cities

print(get_cities('Alaska'))

headers = ['city', 'state']

def fill_headers(headers):
    c = 0
    for h in headers:
        worksheet.cell(column=c, row=0).value = h
        c += 1

fill_headers(headers)
print('done')