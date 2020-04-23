def function_cc(city, country, population=""):
    if population:
        city_country = city.title() + ", " + country.title() + " - population " + str(population)
    else:
        city_country = city.title() + ", " + country.title() 
    return city_country