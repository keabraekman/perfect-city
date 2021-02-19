import sys
from openpyxl import load_workbook


workbook = load_workbook('us-cities-demographics.xlsx')
worksheet = workbook.active


# for row in worksheet.values:
#     print(row[0])



def race_percentage(row):
    if(row[11] == 'Count' or row[5] == 'Total Population'):
        return 0
    else:
        return(int(row[11])/int(row[5]))


def race_name(row):
    return row[10]

def race(row):
    return row[10]

def city(row):
    return row[0]

def population(row):
    if(row[5] == 'Total Population'):
        return 0
    return int(row[5])


# for row in worksheet.values:
#     print(city(row))
#     print(race(row))
#     print(race_percentage(row))
#     print()


# Create dictionaries for each city
# Each city is a key and the value will be 
# ['American Indian and Alaska Native', 
# 'Black or African-American', 
# 'Hispanic or Latino', 
# 'Asian', 
# 'White']

cities = dict()
different_races = []
for row in worksheet.values:
    cities[city(row)] = [0,0,0,0,0,0]


for row in worksheet.values:
    if(race(row) == 'American Indian and Alaska Native'):
        cities[city(row)][0] = race_percentage(row)
    if(race(row) == 'Black or African-American'):
        cities[city(row)][1] = race_percentage(row)
    if(race(row) == 'Hispanic or Latino'):
        cities[city(row)][2] = race_percentage(row)
    if(race(row) == 'Asian'):
        cities[city(row)][3] = race_percentage(row)
    if(race(row) == 'White'):
        cities[city(row)][4] = race_percentage(row)
    cities[city(row)][5] = population(row)


native = 0
black = 0
hispanic = 0.1
asian = 0.3
white = 0.6

minimum_population = 200000

preferences = [0,0,0,1,0,minimum_population]


# minimum_population = 500000
# preferences = [0,0,0.1,0.3,0.6,minimum_population]


delta = dict()

for key in cities:
    delta[key] = [0,0,0,0,0,0]

for row in worksheet.values:
    if(race(row) == 'American Indian and Alaska Native'):
        delta[city(row)][0] = abs(cities[city(row)][0] - preferences[0])
    if(race(row) == 'Black or African-American'):
        delta[city(row)][1] = 3*abs(cities[city(row)][1] - preferences[1])
    if(race(row) == 'Hispanic or Latino'):
        delta[city(row)][2] = abs(cities[city(row)][2] - preferences[2])
    if(race(row) == 'Asian'):
        delta[city(row)][3] = abs(cities[city(row)][3] - preferences[3])
    if(race(row) == 'White'):
        delta[city(row)][4] = abs(cities[city(row)][4] - preferences[4])
    # delta[city(row)][5] = abs(cities[city(row)][5] - preferences[5])
    if(preferences[5] < cities[city(row)][5]):
        delta[city(row)][5] = True
    else:
        delta[city(row)][5] = False
    # print(city(row))
    # print('DELTA = ', delta[city(row)])


total = dict()
for key in delta:
    if(delta[key][5]):
        total[key] = delta[key][0] + delta[key][1] + delta[key][2] + delta[key][3] + delta[key][4]


sorted_values = sorted(total.values()) # Sort the values
sorted_dict = dict()
for i in sorted_values:
    for k in total.keys():
        if total[k] == i:
            sorted_dict[k] = total[k]
            break


ranking = 1
for key in sorted_dict:
    print(ranking, " : ", key)
    ranking = ranking + 1


# Add average weather
# Add state tax
# Crime Rate
# Average age
# Sunny days per year
# Get a better dataset with smaller cities
# Average SAT Score
# Religious preference (mormon check and devil worshipers)
# 





