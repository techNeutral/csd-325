#Cindy Hernandez
#Brett Fuller
#Nardos Gebremedhin
#Elizabeth Hinz
#11/24/2024
#CSD 325  – Assignment 6.2

"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""


import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = '~'  # New symbol for lake

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

def main():
    forest = createnewForestWithLake()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # Fire spreads to neighboring trees (unless there's a lake):
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x + ix, y + iy)) == TREE:
                                if forest.get((x + ix, y + iy)) != LAKE:
                                    nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object:
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createnewForestWithLake():
    """Returns a dictionary for a new forest data structure with a lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    
    # Initialize the forest with trees and empty spaces
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # Add the lake to the forest
    addLakeToForest(forest)
    return forest

def addLakeToForest(forest):
    """Add a rectangular lake to the forest, centered in the middle."""
    # Fixed lake size defined inside this function
    lake_width = 10  # You can change this to any fixed width
    lake_height = 5  # You can change this to any fixed height

    # Center the lake in the forest
    lake_x = int((WIDTH / 2) - (lake_width / 2))  # Centered X position
    lake_y = int((HEIGHT / 2) - (lake_height / 2))  # Centered Y position

    # Fill the area with the lake symbol (~)
    for x in range(lake_x, lake_x + lake_width):
        for y in range(lake_y, lake_y + lake_height):
            forest[(x, y)] = LAKE  # Mark as lake

def displayForest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == LAKE:
                bext.fg('blue')     
                print(LAKE, end='')  # Display lake '~' in blue
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
