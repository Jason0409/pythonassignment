"""COMP6730 question 8.

This should be completed individually.

Author: <University ID> u6261174
Date: <Date> 21/10/2018
"""
import random
import matplotlib.pyplot as plt

from data_and_code.assignment_template import fire_risk, load_bushfire, \
    load_vegetation_type, load_vegetation_density, load_wind_speed


def get_vegetation_type(vegetation_type):
    """this function is used to get the type of the vegetation from a list of lists.
    [[]] -> [] """

    # use a list store the type of vegetation
    vegetation = []

    # travel the list of lists
    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            if vegetation_type[i][j] != '' and vegetation_type[i][j] not in vegetation:
                vegetation.append(vegetation_type[i][j])

    return vegetation


def get_fire_risk_matrix(vegetation_type, vegetation_density, wind_speed):
    """this function is used to get the fire risk matrix from three variables which is
    the type of vegetation, the density of the vegetation, the speed of the wind.
    ([[]],[[]],[[]]) -> [[]]"""

    # use a list to store the fire risk factor
    fire_factor_x=[]

    # travel the list of lists to get the coordinates
    for i in range(len(vegetation_type)):
        fire_factor_y = []
        for j in range(len(vegetation_type[i])):
            fire_factor_y.append(fire_risk(j, i, vegetation_type, vegetation_density, wind_speed))
        fire_factor_x.append(fire_factor_y)

    return fire_factor_x


def plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed):
    """this function is used to plot the graph of relation between the number of each type
    of fired vegetation and the steps. If the vegetation is on fire depends on the fire risk
    of each cell.  ([[]],[[]],[[]],[[]]) ->   """

    # init a set to store the point which is on fire
    initial_fire_point = set()
    # the set of near a point
    near_fire_point = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    # init a step to store step
    steps = []
    # get the fire factor matrix
    fire_factor_x = get_fire_risk_matrix(vegetation_type, vegetation_density, wind_speed)
    # get the types of the vegetation
    vegetation = get_vegetation_type(vegetation_type)

    # build a step list
    for i in range(200):
        steps.append(i)

    # get the initial bushfire
    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            if initial_bushfire[i][j] == '1':
                initial_fire_point.add((i, j))

    # list for storing the number of each type vegetation on fire for all the steps
    vegetation_list = []
    # list for storing the number of each type vegetation on fire
    num_of_vegetation = []

    # get the number of vegetation on fire on step 0
    for i in range(len(vegetation)):
        num = 0
        for point in initial_fire_point:
            if vegetation_type[point[0]][point[1]] == vegetation[i]:
                num += 1
        num_of_vegetation.append(num)

    # copy the initial bushfire
    new = num_of_vegetation.copy()
    # add the number of each type of the vegetation on step 0
    vegetation_list.append(new)

    # simulation of the fire spread
    for step in range(1, len(steps)):
        step_vegetation_list = []
        initial_fire_point_old = initial_fire_point.copy()
        for point_value in set(initial_fire_point):
            for nearpoint in near_fire_point:
                pos_x = point_value[0] + nearpoint[0]
                pos_y = point_value[1] + nearpoint[1]
                if 0 <= pos_x < len(initial_bushfire) and 0 <= pos_y < len(initial_bushfire) and initial_bushfire[pos_x][pos_y] == '0':
                    random_num = 75 * random.random()
                    if random_num < fire_factor_x[pos_x][pos_y]:
                        initial_fire_point.add((pos_x, pos_y))
        new_point = initial_fire_point - initial_fire_point_old
        for i in range(len(vegetation)):
            for new_add_point in new_point:
                if vegetation_type[new_add_point[0]][new_add_point[1]] == vegetation[i]:
                    num_of_vegetation[i] += 1
        step_vegetation_list.extend(num_of_vegetation)
        vegetation_list.append(step_vegetation_list)

    vegetation_list_new = list(map(list, zip(*vegetation_list)))

    # show the graph
    plt.figure(num=len(vegetation))
    plt.title("number of different type vegetation which is fired")
    plt.grid(linestyle="-.")
    plt.xlabel("step")
    plt.ylabel("number")
    for i in range(len(vegetation)):
        plt.plot(steps, vegetation_list_new[i], linewidth=2.0, label=vegetation[i])
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    # If you want something to happen when you run this file,
    # put the code in this `if` block.

    # if you want to plot other map please edit the following code
    # besides the step are in the function plot_fire_spread().
    initial_bushfire1 = load_bushfire("../data_and_code/data/south/initial_2003_bushfire.csv")
    vegetation_type1 = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
    vegetation_density1 = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    wind_speed1 = load_wind_speed("../data_and_code/data/south/wind.csv")
    plot_fire_spread(initial_bushfire1, vegetation_type1, vegetation_density1, wind_speed1)

