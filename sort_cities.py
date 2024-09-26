# Author : Chikwanda Chisha
# Date: 11/05/2022
# Purpose : LAB3
from quicksort import *
from city import City


def compare_population(a, b):
    return a.population >= b.population  # used when sorting according to population


def compare_alpha(a, b):
    return a.city_name <= b.city_name  # used when sorting according to alphabetical order


def compare_latitude(a, b):
    return a.latitude <= b.latitude  # used when sorting according to latitude


city_r = open("world_cities", "r")
city_a = open("city_alpha", "w")
city_p = open("city_population", "w")
city_l = open("city_latitude", "w")
city_list = []
new_city_list = []
for line in city_r:
    info_list = line.strip().split(",")
    city_object = City(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5])
    city_list.append(city_object)

sort(city_list, compare_alpha)

for i in city_list:
    city_a.write(str(i))
    if i == city_list[len(city_list) - 1]:  # to ensure that there is no blank like in the txt file
        pass
    else:
        city_a.write("\n")
city_r.close()

sort(city_list, compare_population)

for i in city_list:
    city_p.write(str(i))
    if i == city_list[len(city_list) - 1]:  # to ensure that there is no blank like in the txt file
        pass
    else:
        city_p.write("\n")

sort(city_list, compare_latitude)

for i in city_list:
    city_l.write(str(i))
    if i == city_list[len(city_list) - 1]:  # to ensure that there is no blank like in the txt file
        pass
    else:
        city_l.write("\n")

city_a.close()
city_l.close()
city_p.close()
