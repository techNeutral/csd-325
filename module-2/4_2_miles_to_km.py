#Brett Fuller
#CSD205 Assignment 4.2
#8/26/2024

#recursive function including try / except block to validate user input.
#this function asks a user to type in the amount of miles they drove.
#Try / except knowledge comes from previous programming classes and experience
#I used floats to allow for decimals
#Once the user enters their info I attempt to convert it to a float and if there is a value error such as a string or null value
#it will sent a ValueError which the except block catches, lets the user know they typed an incorrect value and reprompts them to enter
#their miles driven. Once the user types an acceptable value the finally statement returns the float value.
def get_miles_driven():
    try:
        userInput = input("How many miles did you drive? ")
        number = float(userInput)  
    except(ValueError):
        print(userInput, "is not a number, please try again!")
        #recursively calls the orignal function, will run until an acceptable value is entered.
        number = get_miles_driven()
    finally:
        return number
    

#function to convert miles to kilometers. The function expects a float of miles to be passed and convets it to kilometers and returns the value
#I got the conversion rate off google searches conversion tool
def get_kilometers_from_miles(miles):
    kilometers = miles * 1.60934
    return kilometers

#calls the get_miles_driven() function and sets return value to miles
miles = get_miles_driven()

#calls the get_kilometers_from_miles() and passes the value of miles. Sets the return value to km
km = get_kilometers_from_miles(miles)

#prints miles and kilometers in a readable format.
#as a side note I don't love the output but since the assignment did not explicitly tell me to round to x number of significant digits I printed what I got
print("You drove", miles, "miles or", km, "kilometers!")