# Exercise 15-3 Molecular Motion: Modify 'rw_visual.py' by replacing 'plt.scatter()' with 'plt.plot()'. To simulate the
# path of a pollen grain on the surface of a drop of water, pass in the 'rw.x_values' and 'rw.y_values' and include a
# linewidth argument. Use 5000 instead of 50000 points.


import matplotlib.pyplot as plt
from random_walk import RandomWalk


# Keep making new walks as long as program is active.
while True:
    # Make random walk and plot the points.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window.
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=0.5)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (Y/N) ")
    if keep_running.lower() == "n":
        break


# Exercise 15-4 Modified Random Walks: In the class 'RandomWalks', modify the lists 'x_step' and 'y_step' to see what
# happens to the overall shape of your walks.
# CHANGES ADDED: 'x_direction' and 'y_direction' - switched '-1' to 0.
#                'x_distance' and 'y_distance' - added values up to 8.
#                Changes resulted in plotting a straight line as the possibilities of directions are now limited.


from random import choice


class RandomWalk:
    """Generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction and how far to go.
            x_direction = choice([1, 0])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, 0])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# Exercise 15-5 Refactoring: The method 'fill_walk()' is lengthy. Create a new method called 'get_step()' to determine
# the direction and distance for each step, then calculate the step. You should end up with two calls to 'get_step()' in
# 'fill_walk()'.


class RandomWalk:
    """Generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Chose distance and direction, then create value for step and return it."""

        # Chose direction: 1 = right or up, -1 left or down (depending on axis).
        direction = choice([1, -1])
        # Chose distance for step.
        distance = choice([0, 1, 2, 3, 4])

        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
