import sys
import time
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# workbook = Workbook('perfect-city.xlsx')
workbook = Workbook()
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

column_titles = ['City', 'State', 'White', 'Hispanic', 'Black', 'Asian', 
'American Indian', 'Other', 'Pacific Islander', 'Two or more races', 'Population', 
'Average Age', 'Median Income per Capita', 'Median Income per Household', 
'Unemployment', 'Poverty level', 'Trump', 'Biden', 'Average BMI', 'Overweight percentage',
'number of sunny days', 'percentage of women', 'Violent Crime', 'Population Density', 'tax rate']

def get_html(url):
    re = requests.get(url)
    return BeautifulSoup(re.text, 'html.parser')

def get_cities(state):
    soup = get_html('https://www.city-data.com/city/' + state + '.html')
    cities = []
    for c in soup.find_all('tr', {'class': 'rB'}):
        cities.append(c.find_all('td')[1].find_all('a')[0].contents[0])
    return cities


def fill_headers(titles):
    column = 1
    for t in titles:
        worksheet.cell(row = 1, column = column, value = t)
        column += 1


def create_city_list():
    cities = []
    for s in states:
        to_add = get_cities(s)
        for c in to_add:
            cities.append(c.split(',')[0])
    return cities


def fill_cities_column(cities):
    row = 2
    for c in cities:
        worksheet.cell(row = row, column = 1, value = c)
        row += 1


def number_of_cities(state):
    return len(get_cities(state))


def find_first_empty_row(column):
    r = 1
    while(worksheet.cell(row = r, column = column).value is not None):
        r += 1
    return r




def fill_state():
    for s in states:
        number_of_rows = number_of_cities(s)
        first_empty_row = find_first_empty_row(2)
        for i in range(number_of_rows):
            worksheet.cell(row = first_empty_row+i, column = 2, value = s)
        workbook.save('perfect-city.xlsx')

print('fill_headers')
fill_headers(column_titles)
print('cities')
cities = create_city_list()
print('fill_cities_column')
fill_cities_column(cities)
print('fill_state')
fill_state()


workbook.save('perfect-city.xlsx')


