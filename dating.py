import sys
from openpyxl import load_workbook


workbook = load_workbook('us-cities-demographics.xlsx')
worksheet = workbook.active

def race_percentage(row):
    if(row[11] == 'Count' or row[5] == 'Total Population'):
        return 0
    else:
        return(int(row[11])/int(row[5]))

def female_percentage(row):
    if(row[3] == 'Male Population') or row[3] == None or row[4]==None:
        return 0
    else:
        return(int(row[4]) / (int(row[3])+int(row[4])))

def average_age(row):
    if(row[3] == 'Median Age'):
        return 0
    else:
        return(row[2])

def city(row):
    return row[0]

cities = dict()
different_races = []
for row in worksheet.values:
    cities[city(row)] = {}

# female percentage
# native = 0
# black = 0.0
# hispanic = 0.0
# asian = 0.3
# white = 0.7
# Population


# math to compute best city:
# Most white and asian women in highest female percentage at younger average age
# Idea : white percentage * female percentage + asian percentage * female percentage

ideal_average_age = 30

for row in worksheet.values:
    if row[10] == 'White':
        cities[city(row)]['whiteP'] = race_percentage(row)
    if row[10] == 'Asian':
        cities[city(row)]['asianP'] = race_percentage(row)
    cities[city(row)]['femaleP'] = female_percentage(row)
    cities[city(row)]['age'] = female_percentage(row)
    print(cities[city(row)])
    if 'femaleP' in cities[city(row)] and 'whiteP' in cities[city(row)] and 'asianP' in cities[city(row)]:
        cities[city(row)]['result'] = cities[city(row)]['femaleP'] * (cities[city(row)]['whiteP']+cities[city(row)]['asianP'])


# for c in cities:
#     cities[city(row)]['result'] = cities[city(row)]['femaleP'] * (cities[city(row)]['whiteP']+cities[city(row)]['asianP']) / abs(average_age(row)-ideal_average_age)


print(cities['Flagstaff'])


# sorted(answer.items(), key=lambda x: x[1], reverse=True))