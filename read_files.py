# Author : Chikwanda Chisha
# Date: 11/05/2022
# Purpose : LAB3
from city import City

city_r = open("world_cities", "r")
city_w = open("cities_out", "w")
city_list = []
for line in city_r:
    info_list = line.strip().split(",")  # strips the line of whitespaces and splits it by commas
    city_object = City(info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5])
    city_list.append(city_object)  # adds city object to city_list

for data in city_list:
    if data == city_list[len(city_list) - 1]:  # to ensure that there is no blank like in the txt file
        city_w.write(str(data))
    else:
        city_w.write(str(data) + "\n")
city_r.close()
city_w.close()
