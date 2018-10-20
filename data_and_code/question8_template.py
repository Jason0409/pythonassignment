"""COMP6730 question 8.

This should be completed individually.

Author: <University ID>
Date: <Date>
"""
import random
import matplotlib.pyplot as plt

from data_and_code.assignment_template import fire_risk, load_bushfire, \
    load_vegetation_type, load_vegetation_density, load_wind_speed


def plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed):
    steps = 100
    fire_factor_x = []
    fire_factor_y = []
    initial_fire_point = set()
    vegetation = ["Open Forest", "Forest", "Open Woodland", "Woodland",
                  "Pine Forest", "Arboretum", "Grassland", "Shrubland",
                  "Golf Course", "Urban Vegetation", "Vineyard"]
    num_of_vegetation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    vegetation_list = []

    for i in range(len(initial_bushfire)):
        for j in range(len(initial_bushfire[i])):
            if initial_bushfire[i][j] == '1':
                initial_fire_point.add((i, j))

    # all direction around point(x,y)
    near_fire_point = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for i in range(len(vegetation_type)):
        for j in range(len(vegetation_type[i])):
            fire_factor_y.append(fire_risk(j, i, vegetation_type, vegetation_density, wind_speed))
        fire_factor_x.append(fire_factor_y)

    for step in range(steps):
        step_vegetation_list = []
        for point_value in set(initial_fire_point):
            for nearpoint in near_fire_point:
                pos_x = point_value[0] + nearpoint[0]
                pos_y = point_value[1] + nearpoint[1]
                if 0 <= pos_x < len(initial_bushfire) and 0 <= pos_y < len(initial_bushfire) and \
                        initial_bushfire[pos_x][pos_y] == '0':
                    random_num = 75 * random.random()
                    if random_num < fire_factor_x[pos_x][pos_y]:
                        initial_fire_point.add((pos_x, pos_y))
                        for i in range(len(num_of_vegetation)):
                            if vegetation_type[pos_x][pos_y] == vegetation[i]:
                                num_of_vegetation[i] = num_of_vegetation[i] + 1
        step_vegetation_list.extend(num_of_vegetation)
        vegetation_list.append(step_vegetation_list)
    print(vegetation_list)

    plt.plot(range(steps), [row[0] for row in vegetation_list], 'r-x', label="Open Forest")
    plt.plot(range(steps), [row[1] for row in vegetation_list], 'bo', label="Forest")
    plt.plot(range(steps), [row[2] for row in vegetation_list], 'yo', label="Open Woodland")
    plt.plot(range(steps), [row[3] for row in vegetation_list], 'r*', label="Woodland")
    plt.plot(range(steps), [row[4] for row in vegetation_list], 'b', label="Pine Forest")
    plt.plot(range(steps), [row[5] for row in vegetation_list], 'y', label="Arboretum")
    plt.plot(range(steps), [row[6] for row in vegetation_list], 'r', label="Grassland")
    plt.plot(range(steps), [row[7] for row in vegetation_list], 'r', label="Shrubland")
    plt.plot(range(steps), [row[8] for row in vegetation_list], 'r', label="Golf Course")
    plt.plot(range(steps), [row[9] for row in vegetation_list], 'r', label="Urban Vegetation")
    plt.plot(range(steps), [row[10] for row in vegetation_list], 'r', label="Vineyard")

    plt.xlabel('Steps')
    plt.ylabel('Number of cells')
    plt.legend()  # 展示图例
    plt.title('Number of cells on fire over time for each vegetation type')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
    # plt.savefig("sinx.jpg")


if __name__ == '__main__':
    initial_bushfire = load_bushfire("../data_and_code/data/south/initial_2003_bushfire.csv")
    final_bushfire = load_bushfire("../data_and_code/data/south/2003_bushfire.csv")
    vegetation_type = load_vegetation_type("../data_and_code/data/south/vegetation_type.csv")
    vegetation_density = load_vegetation_density("../data_and_code/data/south/vegetation_density.csv")
    wind_speed = load_wind_speed("../data_and_code/data/south/wind.csv")
    plot_fire_spread(initial_bushfire, vegetation_type, vegetation_density, wind_speed)
