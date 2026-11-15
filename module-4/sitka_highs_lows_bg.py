# Name: Brian Guadron
# Date: 11/18/2026
# Assignment Number - Module 4.2 Assignment
#
# Purpose - The purpose is to develop a Python program that reads weather data from the sitka_weather_2018_simple.csv file and allows the users to
# view a graph of the high or low temperatures for Sitka, Alaska, in 2018. The user can choose which graph he wants to see today or end the
# program.
#
# Resource: I used Quick start guide from Matplotlib and stackoverflow posts to complete the assignment.
# Matplotlib url : https://matplotlib.org/stable/users/explain/quick_start.html
# stackoverflow url: https://stackoverflow.com/questions/69109608/indexing-without-knowing-the-index-of-a-row-only-the-title-of-the-row-index
#

import csv

# Imported the sys library to be able to exit when the user menu option equal exit
import sys
from datetime import datetime

from bext import title
from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

    # Getting the low temperatures from this file
        low = int(row[6])
        lows.append(low)

# Added while loop to displays the weather menu options
# It will keep asking the user for the menu option to match highs, lows or exit
while True:
    print("*************** The Weather Temperature Menu Options ***************")
    print()
    print("Please enter 'highs' to see the high temperatures chart.")
    print("Please enter 'lows' to see the low temperatures chart.")
    print("Please enter 'exit' to end and exit the program.")
    print()

    # Asking the user to make a choice that gets convert to lower case without any leading whitespace
    user_input_option = input("What option would you like to see today? ").lower().strip()

    # If the user enter highs, it plots the high temperatures
    if user_input_option == 'highs':
        # Plot the high temperatures.
        # plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        title = "Daily high temperatures - 2018"

    # If the user enter lows, it plots the low temperatures
    elif user_input_option == 'lows':
        # Plot the low temperatures.
        # plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='blue')
        title = "Daily low temperatures - 2018"

    # If the user enter exits, it prints a thank-you message, and it ends the execution
    elif user_input_option == 'exit':
        print("We thank you for using our services today. Have a great day and goodbye!!.")
        print()
        sys.exit()

    # If the user types something else, it prints a message asking for a valid entry
    else:
        print(" Your selection is invalid. Please try again by entering highs, lows, or exit")
        print()
        continue

    # Format plot.
    # Now it is part of the while loop
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

