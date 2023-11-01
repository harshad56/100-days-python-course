import math
height_wall = int(input("height of the wall:"))
widht_wall = int(input("width of the wall:"))
cover_the_wall = int(input("how many times you cover:"))


def my_funtion(height, width, cover):
    area = height*width
    num_of_cans = math.ceil(area/cover)
    print(f"number of cans is required:{num_of_cans}")


my_funtion(height=height_wall, width=widht_wall, cover=cover_the_wall)
