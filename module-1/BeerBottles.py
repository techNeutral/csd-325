#Brett Fuller
#CSD325 Assignment 1.3 - bottles of beer
#10/25/2024

#The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
#Once the count is down to 1, change lyrics to show "1 bottle of beer..."
def countDown(bottles):
    while(bottles > 0):
        if bottles > 2:
            bottleString = "bottles"
            tempBottleString = "bottles"
        elif bottles == 2:
            bottleString = "bottles"
            tempBottleString = "bottle"
        else:
            bottleString = "bottle"
            tempBottleString = "bottles"
        print(f"{bottles} {bottleString} of beer on the wall, {bottles} {bottleString} of beer.\n") 
        bottles -= 1
        print(f"Take one down and pass it around, {bottles} {tempBottleString} of beer on the wall\n\n")
        



#Ask the user how many bottles of beer are on the wall.
isInt = False
while  isInt == False:   
    try:
        numberOfBottles = input("Enter number of Bottles: ")
        numberOfBottles = int(numberOfBottles)
    except (ValueError):
        print("you did not enter an integer")
        print()
    else:
        isInt = True

#Pass that input to a function that manages the countdown.   
countDown(bottles=numberOfBottles)
#At the end of the countdown, get back to the main program and remind the user to buy more beer.help
print("Time to buy more beer.")
        

