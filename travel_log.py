# Day 9 - Exercise 2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(country_visited, times_visited, cities_visited):
    new_entry = {}
    new_entry["country"] = country_visited
    new_entry["visits"] = times_visited
    new_entry["cities"] = cities_visited
    travel_log.append(new_entry)

# alternatively most efficient way is
# new_entry = {"country": country_visited, "visits": times_visited, "cities": cities_visited}
# travel_log.append(new_entry)

# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
