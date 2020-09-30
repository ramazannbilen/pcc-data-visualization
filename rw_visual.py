import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:

    # Make a random_walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()
    #plt.scatter(rw.x_values, rw.y_values, s=1)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)

    plt.show()
    # plt.savefig("random_walk_plot.png", bbox_inches="tight")
    keep_running = input("Make another walk? (y/n) : ")
    if keep_running == 'n':
        break
