import json
from country_codes import get_country_code


# Load the data into a list.
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dic in pop_data:
    if pop_dic["Year"] == "2010":
        country_name = pop_dic["Country Name"]
        population = int(float(pop_dic["Value"]))
        code = get_country_code(country_name)
        if code:
            print(f"{country_name}: {population}")
        else:
            print(f"ERROR - {country_name}")
