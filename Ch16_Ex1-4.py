# Exercise 16-2 Sitka-Death Valley Comparison: To accurately compare the temperature range in Sitka to that of Death
# Valley, you need identical scales on the y-axis. Change the settings for the y-axis on one or both of the charts and
# make a direct comparison between temperature ranges in Sitka and Death Valley. Try plotting both data sets on the same
# chart.


import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_dv, highs_dv, lows_dv = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates_dv.append(current_date)
            highs_dv.append(high)
            lows_dv.append(low)


filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_s, highs_s, lows_s = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates_s.append(current_date)
            highs_s.append(high)
            lows_s.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_dv, highs_dv, c='red', alpha=0.5)
plt.plot(dates_dv, lows_dv, c="blue", alpha=0.5)
plt.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.5)

plt.plot(dates_s, highs_s, c='red', alpha=0.5)
plt.plot(dates_s, lows_s, c="blue", alpha=0.5)
plt.fill_between(dates_s, highs_s, lows_s, facecolor='blue', alpha=0.5)


plt.title("Daily high and low temperatures - 2014\nComparison between Sitka and Death Valley", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


# Exercise 16-3 Rainfall: Choose any location and make a visualization that plots its rainfall. Start by focusing on one
# month's data and, once your code is working, run it for a full year's data.


with open("death_valley_2014.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precipitation = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = row[19]
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            precipitation.append(rain)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precipitation, c='blue')

plt.title("Rainfall in Death Valley - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (In)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()


# Exercise 16-4 Explore: Generate a few more visualizations that examine any other weather aspect for any location.
