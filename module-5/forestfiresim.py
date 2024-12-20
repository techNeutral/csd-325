"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation"""

import random, sys, time, math

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
LAKE = '~'

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01  # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01  # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

WATER_BLOCKS_LINE_OF_SITE = True

def main():
    forest = createNewForest()
    forest = addLakeToForest(forest)
    bext.clear()
    

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here:
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
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    #set default range for checking firespread
                    xRxLow = -1
                    xRxHigh = 2
                    yRyLow = -1
                    yRyHigh = 2
                    #if we decide diagonals are blocked by lakes override the above values if needed
                    if WATER_BLOCKS_LINE_OF_SITE == True:
                        if forest.get((x - 1, y)) == LAKE:
                            xRxLow = 0
                        if forest.get((x + 1, y)) == LAKE:
                            xRxHigh = 1
                        if forest.get((x, y-1)) == LAKE:
                            yRyLow = 0
                        if forest.get((x, y+1)) == LAKE:
                            yRyHigh = 1

                    for ix in range(xRxLow, xRxHigh):
                        for iy in range(yRyLow, yRyHigh):
                            # Fire spreads to neighboring trees:
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object: - This also accounts for the lake
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)

#function to create a randomly sized length in the middle of the map
def addLakeToForest(forest):
    if WIDTH > 14:
        lakeWidth = random.randint(1, 12)
    elif WIDTH > 2:
        lakeWidth = random.randint(1, (WIDTH - 2))
    else:
        lakeWidth = 1
    if HEIGHT > 14:
        lakeHeight = random.randint(1, 12)
    elif HEIGHT > 2:
        lakeHeight = random.randint(1, (HEIGHT - 2))
    else:
        lakeHeight = 1
    
    xStart = math.floor(WIDTH / 2) - math.floor(lakeWidth / 2)
    if(xStart <= 0 ):
        xStart = 1
    xEnd = xStart + lakeWidth

    yStart = math.floor(HEIGHT / 2) - math.floor(lakeHeight / 2)
    if(yStart <= 0):
        yStart = 1
    yEnd = yStart + lakeHeight
    
    for x in range(xStart, xEnd):
        for y in range(yStart, yEnd):
            forest[(x,y)] = LAKE
    
    return forest



def createNewForest():
    """Returns a dictionary for a new forest data structure."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.
    return forest


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
                print(LAKE, end='')            	
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')          
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
