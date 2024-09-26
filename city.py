# Author : Chikwanda Chisha
# Date: 11/05/2022
# Purpose : LAB3
class City:
    def __init__(self, country_code, city_name, city_region, population, latitude, longitude):
        self.country_code = str(country_code)
        self.city_name = str(city_name)
        self.city_region = str(city_region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"{self.city_name},{self.population},{self.latitude},{self.longitude}"
