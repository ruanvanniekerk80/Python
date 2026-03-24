# 11-1. City, Country: 
def get_city_country(city,country):
   """Return a string like 'Santiago,Chile'."""
   return f"{city.title()}, {country.title()}"

get_city_country("Santiago","Chile")

# 11-2. Population:
def get_city_country(city, country, population):
    """Return a string like 'Santiago, Chile – population 5000000'."""
    return f"{city.title()}, {country.title()} – population {population}"

