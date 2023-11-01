travel_log = [
    {"country": "France",
     "visits": 12,
     "city_visted": ["paris", "lile", "djanho"]},


    {"country": "Germeny",
     "visits": 12,
     "city_followup": ["Berlin", "handburg", "strupat"]},
]


# Todo: write a function that will allow new country
# to be added to the travel_log.

def add_new_country(country_visited, times_visted, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visted
    new_country["city_visited"] = cities_visited

    travel_log.append(new_country)


add_new_country("russia", 12, ["mossow", "saint paintburg"])
print(travel_log)
