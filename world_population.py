import json
from pygal_maps_world.maps import World
from country_codes import get_country_code


# Load the data into a list.
filename = "population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_population = {}
for pop_dic in pop_data:
    if pop_dic["Year"] == "2010":
        country_name = pop_dic["Country Name"]
        population = int(float(pop_dic["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population

wm = World()
wm.title = "World Population in 2010, by Country"
wm.add("2010", cc_population)

wm.render_to_file("world_population.svg")
