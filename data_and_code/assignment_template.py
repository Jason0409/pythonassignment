"""COMP1730/6730 assignment S2 2018.

Coauthors: <u6261174>, <u6068466>, <u6323315>
Date: <05/10/2018>
"""

from visualise import show_vegetation_type
from visualise import show_vegetation_density
from visualise import show_wind_speed
from visualise import show_bushfire
from visualise import show_fire_risk
import csv
import math


# The following functions must return the data in the form of a
# list of lists; the choice of data type to represent the value
# in each cell, for each file type, is up to you.

def load_vegetation_type(filename):
    with open(filename) as vegetation_type_csvfile:
        reader = csv.reader(vegetation_type_csvfile)
        # get row from table
        vegetation_type_table = [row for row in reader]
    return vegetation_type_table


def load_vegetation_density(filename):
    with open(filename) as vegetation_density_csvfile:
        reader = csv.reader(vegetation_density_csvfile)
        # get row from table
        vegetation_density_table = [row for row in reader]
    return vegetation_density_table


def load_wind_speed(filename):
    with open(filename) as wind_speed_csvfile:
        reader = csv.reader(wind_speed_csvfile)
        # get row from table
        wind_speed_table = [row for row in reader]
    return wind_speed_table


def load_bushfire(filename):
    with open(filename) as bushfire_csvfile:
        reader = csv.reader(bushfire_csvfile)
        # get row from table
        bushfire_table = [row for row in reader]
    return bushfire_table


# The argument to this function is a wind speed map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_wind_speed
# function.

def highest_wind_speed(wind_speed):
    new_data = []
    for i in range(len(wind_speed)):
        new_data.append(max(wind_speed[i]))
    return max(new_data)


# The argument to this function is a vegetation type map, in the
# form of a list of lists; it is the same data structure that
# is returned by your implementation of the load_vegetation_type
# function.

def count_cells(vegetation_type):
    pass


# The arguments to this function are a vegetation type map and
# a vegetation density map, both in the form of a list of lists.
# They are the same data structure that is returned by your
# implementations of the load_vegetation_type and load_vegetation_density
# functions, respectively.

def count_area(vegetation_type, vegetation_density):
    pass


# The arguments to this function are:
# x and y - integers, representing a position in the grid;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def fire_risk(x, y, vegetation_type, vegetation_density, wind_speed):
    # x is the column and y is the row
    dif_x_arr = []
    dif_y_arr = []
    fire_radius =0
    # fire_radius is the radius of fire impact
    if wind_speed[y][x]!='':
        fire_radius = math.floor(float(wind_speed[y][x]))
    for dif_y in range(-fire_radius, fire_radius + 1):
        for dif_x in range(-fire_radius, fire_radius + 1):
            if (dif_y * dif_y + dif_x * dif_x <= fire_radius * fire_radius):
                dif_x_arr.append(dif_x)
                dif_y_arr.append(dif_y)

    # sum all of the risk factor
    sum_risk_factor = 0

    for dif_y in range(0, len(dif_y_arr)):
        pos_x = x + dif_x_arr[dif_y]
        pos_y = y + dif_y_arr[dif_y]
        if pos_y >= 0 and pos_y < len(vegetation_type) and pos_x >= 0 and pos_x < len(vegetation_type[pos_y]):
            if (vegetation_type[pos_y][pos_x] == "Shrubland" or vegetation_type[pos_y][pos_x] == "Pine Forest"):
                # print(sum_risk_factor)
                sum_risk_factor = sum_risk_factor + math.sqrt(0.2 + float(vegetation_density[pos_y][pos_x]))
            elif (vegetation_type[pos_y][pos_x] == "Arboretum"):
                sum_risk_factor = sum_risk_factor + math.sqrt(0.1 + float(vegetation_density[pos_y][pos_x]))
            elif (vegetation_type[pos_y][pos_x] == "Urban Vegetation" or vegetation_type[pos_y][pos_x] == "Golf Course"):
                sum_risk_factor = sum_risk_factor + math.sqrt(0.05 + float(vegetation_density[pos_y][pos_x]))
            else:
                if (vegetation_density[pos_y][pos_x]!=''):
                    sum_risk_factor = sum_risk_factor + math.sqrt(0 + float(vegetation_density[pos_y][pos_x]))

    return sum_risk_factor


# The arguments to this function are an initial bushfile map (a list
# of lists, as returned by your implementation of the load_bushfire
# function), a vegetation type map (as returned by your implementation
# of the load_vegetation_type function), a vegetation density map (as
# returned by your implementation of load_vegetation_density) and a
# positive integer, representing the number of steps to simulate.

def simulate_bushfire(initial_bushfire, vegetation_type, vegetation_density, steps):
    pass


# The arguments to this function are two bushfile maps (each a list
# of lists, i.e., same format as returned by your implementation of
# the load_bushfire function).

def compare_bushfires(bushfire_a, bushfire_b):
    pass


# The arguments to this function are:
# initial_bushfire - an initial bushfile map (a list of lists, same
#   as returned by your implementation of the load_bushfire function);
# steps - a positive integer, the number of steps to simulate;
# vegetation_type - a vegetation type map (as returned by your
#   implementation of the load_vegetation_type function);
# vegetation_density - a vegetation density map (as returned by
#   your implementation of the load_vegetation_density function);
# wind_speed - a wind speed map (as returned by your implementation
#   of the load_wind_speed function).

def simulate_bushfire_stochastic(
        initial_bushfire, steps,
        vegetation_type, vegetation_density,
        wind_speed):
    pass


if __name__ == '__main__':
    # If you want something to happen when you run this file,
    # put the code in this `if` block.
    # veg_density_map = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
    # show_vegetation_density(veg_density_map)
    # wind_speed = load_wind_speed("../data_and_code/data/anu/wind.csv")
    # print(highest_wind_speed(wind_speed))
    # question 4 anu test
    density_map = load_vegetation_density("../data_and_code/data/anu/vegetation_density.csv")
    type_map = load_vegetation_density("../data_and_code/data/anu/vegetation_type.csv")
    wind_speed_map = load_wind_speed("../data_and_code/data/anu/wind.csv")
    show_fire_risk(fire_risk, type_map, density_map, wind_speed_map)
    # question 4 south test
    # density_map = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    # type_map = load_vegetation_density("../data_and_code/data/south/vegetation_type.csv")
    # wind_speed_map = load_wind_speed("../data_and_code/data/south/wind.csv")
    # show_fire_risk(fire_risk, type_map, density_map, wind_speed_map)
