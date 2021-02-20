import sys
import time
import requests
from bs4 import BeautifulSoup


main_url = 'https://www.city-data.com'


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
    target_url = main_url + '/city/' + s + '.html'
    print(target_url)


