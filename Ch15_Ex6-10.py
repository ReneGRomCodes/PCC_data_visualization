# Exercise 15-6 Automatic Labels: Modify 'die_visual.py' and 'dice_visual.py' by replacing the list that sets the value
# of 'hist_.x_labels' with a loop to generate the list automatically. If you're comfortable with list comprehensions,
# try replacing the other for-loops with comprehensions as well.
# MADE ADDITIONAL CHANGES TO MAKE THE PROGRAM MORE FLEXIBLE.


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
