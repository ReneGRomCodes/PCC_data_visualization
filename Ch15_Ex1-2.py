# Exercise 15-1 Cubes: Plot the first five cubic numbers, then plot the first 5000 cubic numbers.
# Exercise 15-2 Colored Cubes: Apply a colormap to your cubes plot.


import matplotlib.pyplot as plt


input_values = list(range(1, 5001))
cubes = [x**3 for x in input_values]

plt.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Reds)

plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
