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
    pass


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
    pass


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
    pass
