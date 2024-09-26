# Author : Chikwanda Chisha
# Date: 11/05/2022
# Purpose : LAB3
from cs1lib import *

CR = 4
WIN_H = 360
WIN_W = 720
SCALE = WIN_W/WIN_H
timer = 0
n = int(input("How many of most populous cities do you want to see? "))  # allows to input the number of cities you want
city_pop = open("city_population", "r")
lat = []
long = []
for line in city_pop:
    data_list = line.strip().split(",")
    lat.append(float(data_list[2]))  # appends to the latitude list as a float
    long.append(float(data_list[3]))  # appends to the longitude list as a float
city_pop.close()


def main_draw():
    global timer  # so that it can be changed in the main draw and the starting value t=0 is read once
    img = load_image("world.png")
    draw_image(img, 0, 0)
    set_fill_color(1, 0, 0)
    set_stroke_color(1, 0, 0)
    for i in range(timer):
        draw_circle(long[i] * SCALE + WIN_W // 2, WIN_H // 2 - lat[i] * SCALE, CR)
        if timer == n:  # enables the animation effect
            timer = 1
    timer += 1          # enables continuous animation effect


start_graphics(main_draw, height=WIN_H, width=WIN_W)
