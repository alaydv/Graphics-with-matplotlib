"""Get the population for differents parts of time"""
from functools import reduce

def get_population_year(dictionary):
    year_country = {
        '2022': int(dictionary['2022 Population']),
        '2020': int(dictionary['2020 Population']),
        '2015': int(dictionary['2015 Population']),
        '2010': int(dictionary['2010 Population']),
        '2000': int(dictionary['2000 Population']),
        '1990': int(dictionary['1990 Population']),
        '1980': int(dictionary['1980 Population']),
        '1970': int(dictionary['1970 Population']),
    }
    labels = year_country.keys()
    values = year_country.values()

    return labels, values


def get_population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result


def get_population_for_world(data, column='Country/Territory'):
    result = {item[column]: item['World Population Percentage'] for item in data}
    labels = result.keys()
    values = result.values()
    return labels, values


def get_population_by_continent(data):
    result = reduce(lambda dic, dat: {**dic, dat['Continent']:dic.get(dat['Continent'], 0) + float(dat['World Population Percentage'])}, data, {})
    labels = result.keys()
    values = result.values()
    return labels, values