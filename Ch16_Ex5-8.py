# Exercise 16-5 All Countries: On the population map we made in this section, our program couldn't automatically find
# two-letter codes for about 12 countries. Work out which countries are missing codes and look through the
# 'COUNTRIES' dictionary for the codes. Add an 'if-elif-else' block to 'get_country_code()' so it returns the
# correct country code values for these specific countries.


# SOLUTION IMPLEMENTED IN 'COUNTRY_CODES.PY'!!!


# Exercise 16-6 Gross Domestic Product: Download the JSON version of the GDP data set from the 'Open Knowledge
# Foundation' and plot the GDP for each country in the world for the most recent year in the dataset.


import json
import csv
from pygal_maps_world.maps import World
from country_codes import get_country_code


# Load the data into a list.
filename = "global_gdp.json"
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
cc_gdp = {}
for gdp_dic in gdp_data:
    if gdp_dic["Year"] == "2014":
        country_name = gdp_dic["Country Name"]
        gdp = int(float(gdp_dic["Value"]) / 1_000_000_000)
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp


wm = World()
wm.title = "GDP in 2014, by Country\nin Billion USD"
wm.add("", cc_gdp)

wm.render_to_file("world_gdp.svg")



# Exercise 16-7 Choose Your Own Data: The World Bank maintains data sets that are broken down for information on each
# country worldwide. Go to http://www.data.worldbank.org/indicator and find a data set that looks interesting and
# download it as CSV file. Write a program that generates a dictionary with Pygal's two-letter country codes as its keys
# and your chosen data from the file as its values, then plot the data on a 'Worldmap' and style the map as you like.


# Load the data into a list.
filename = "access_to_electricity_in_percent.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    electric = {}
    for row in reader:
        country_name = row[0]
        electrification_str = row[65]
        try:
            electrification = int(float(electrification_str))
            code = get_country_code(country_name)
            electric[code] = electrification
        except ValueError:
            continue

wm = World()
wm.title = "Access to electricity (2021), by Country\nin %"
wm.add("", electric)

wm.render_to_file("access_to_electricity.svg")



# Exercise 16-8 Testing the 'country_codes' Module: When we wrote the 'country_codes' module, we used 'print' statements
# to check whether the 'get_country_code()' function worked. Write a proper test for this function using what you
# learned in chapter 11.
