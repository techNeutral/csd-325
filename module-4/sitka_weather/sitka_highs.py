#Brett Fuller
#CSD325 Assignment 4.2 - Sitka Highs
#11/10/2024

import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    #BF - Added lows to the data as well
    dates, highs, lows= [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        #BF - adding lows
        low = int(row[6])
        lows.append(low)

#BF - Create loop to get input from user

#BF - variable to exit loop if users selects quit
exitLoop = False
while exitLoop == False:
    #BF - variable that allows the program to skip displaying graph if certain conditions are met
    skip = False
    #BF - get user input
    userInput = input("Press 1 or type highs for highs, Press 2 or type lows for lows, or type q or quit for quit: ").lower()
    #BF - sets variables to necessary values for high temp graph
    if userInput == '1' or userInput == 'highs':
        temps = highs
        color = 'red'
        title = "Daily high temperatures - 2018"
    #BF - sets variables to necessary values for low temp graph
    elif userInput == '2' or userInput == 'lows':
        temps = lows
        color = 'blue'
        title = "Daily low temperatures - 2018"
    #BF - allows user to quit the program
    elif userInput == 'q' or userInput == 'quit':
        exitLoop = True
        skip = True
    #BF - handles unexpected input
    else:
        print(userInput, "is not an accepted input")
        skip = True
    
    #logic to skip displaying grapgh if user requests to quit or enters bad data
    if quit != True and skip != True:
        #BF - Plot the user selected temperatures using the values set above.
        #plt.style.use('seaborn')
        fig, ax = plt.subplots()
        ax.plot(dates, temps, c=color)

        # Format plot.
        plt.title(title, fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        plt.show()
