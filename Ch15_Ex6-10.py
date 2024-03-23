# Exercise 15-6 Automatic Labels: Modify 'die_visual.py' and 'dice_visual.py' by replacing the list that sets the value
# of 'hist_.x_labels' with a loop to generate the list automatically. If you're comfortable with list comprehensions,
# try replacing the other for-loops with comprehensions as well.
# MADE ADDITIONAL CHANGES TO MAKE THE PROGRAM MORE FLEXIBLE.


import pygal
from die import Die


die_1 = Die()
die_2 = Die()

# List of Die objects.
dice = [die_1, die_2]
# Establish number of dice.
n_dice = len(dice)

# List comprehension for results.
results = [sum(die.roll() for die in dice) for _ in range(1000)]

# Generator expression for max_result. '+ 1' added to account for offset in later use.
max_result = sum(die.num_sides for die in dice) + 1

# List comprehension for frequencies.
frequencies = [results.count(value) for value in range(n_dice, max_result)]

# List comprehension for x_labels.
x_labels = [x + n_dice for x in range(max_result - n_dice)]


# Exercise 15-7 Two D8: Create a simulation showing what happens if you roll two eight-sided dice 1000 times. Increase
# the number of rolls gradually until you start to see the limits of your system's capabilities.


die_1 = Die(8)
die_2 = Die(8)

dice = [die_1, die_2]
n_dice = len(dice)

results = [sum(die.roll() for die in dice) for _ in range(1000)]  # My machine starts sweating at 10,000,000.
max_result = sum(die.num_sides for die in dice) + 1

frequencies = [results.count(value) for value in range(n_dice, max_result)]

hist = pygal.Bar()
hist.x_labels = [x + n_dice for x in range(max_result - n_dice)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('exercise_15-7.svg')


# Exercise 15-8 Three Dice: If you roll three D6 dice, the smallest number you can roll is 3 and the largest 18. Create
# Visualization that shows what happens when you roll three D6 dice.


die_1 = Die()
die_2 = Die()
die_3 = Die()

dice = [die_1, die_2, die_3]
n_dice = len(dice)

results = [sum(die.roll() for die in dice) for _ in range(1000)]
max_result = sum(die.num_sides for die in dice) + 1

frequencies = [results.count(value) for value in range(n_dice, max_result)]

hist = pygal.Bar()
hist.x_labels = [x + n_dice for x in range(max_result - n_dice)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('exercise_15-8.svg')


# Exercise 15-9 Multiplication: When you roll two dice, you usually add the two number together to get the result.
# Create a visualization that shows what happens if you multiply these numbers instead.


die_1 = Die()
die_2 = Die()

dice = [die_1, die_2]
n_dice = len(dice)

results = [die_1.roll() * die_2.roll() for _ in range(1000)]
max_result = die_1.roll() * die_2.roll() + 1

frequencies = [results.count(value) for value in range(n_dice, max_result)]

hist = pygal.Bar()
hist.x_labels = [x + n_dice for x in range(max_result - n_dice)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file('exercise_15-9.svg')


# Exercise 15-10 Practicing with Both Libraries: Try using 'matplotplib' to make a die-rolling visualization and pygal
# to make a visualization for a random walk.
