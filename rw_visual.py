import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Keep making new walks as long as program is active.
while True:
    # Make random walk and plot the points.
    rw = RandomWalk(100_000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (Y/N) ")
    if keep_running.lower() == "n":
        break
