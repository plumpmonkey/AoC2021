#!/usr/bin/env python

import os
import numpy as np

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


def parts1_and_2(grid, fold_list, width, height):
    print("Part 1:")

    # Loop through the fold list
    for fold in fold_list:
        for axis, line in fold.items():
            if axis == "y":
                # For a Y-based fold, copy the last line into the first line
                # using a logical OR. Repeat for penultimate line into second line, etc
                for y in range(line +1):
                    for x in range(width):
                        grid[y,x] = np.logical_or(grid[y,x], grid[height- 1 -y,x])

                # Set the new height of the grid
                height = line
            else:
                # For an X-based fold, copy the last column into the first column
                # using a logical OR. Repeat for penultimate column into second column, etc
                for y in range(height):
                    for x in range(line+ 1):
                        grid[y,x] = np.logical_or(grid[y,x], grid[y,width - 1 -x])

                # Set the new width of the grid
                width = line

            # Make a smaller grid and copy the old grid into the new grid
            new_grid = np.zeros((height, width), dtype=int)
            for y in range(height):
                for x in range(width):
                    new_grid[y,x] = grid[y,x]

            grid = new_grid
            print(f"  Folding axis {axis} on line {line} - Number of points after fold = {np.sum(grid)}")


    # All folds complete. Print out the points we have left.
    # Construct a string denoting a # for a dot and a space for a 0.
    text = ""
    for y in range(height):
        for x in range(width):
            if(grid[y,x] == 1):
                text += "#"
            else:
                text += " "
        text+='\n'

    print(text)

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        # Read the file. Use the double line break to split the two parts
        # of the input. We can then process these separately
        dots, folds = f.read().split('\n\n')

        # Convert the dot locations into a list - [[x,y], [x,y]...]
        dot_list = [list(map(int, position.split(','))) for position in dots.split('\n')]

        # Determine the size of the grid (assumes the last line is populated with an entry!)
        width = (max(dot_list, key=lambda x: x[0]))[0] + 1
        height = (max(dot_list, key=lambda x: x[1]))[1] + 1

        # Create an empty numpy grid
        grid = np.zeros((height, width), dtype=int)

        # Populate the initial dots into the grid
        for x, y in dot_list:
            grid[y, x] = 1

        # Now parse the folds.
        # Example entry - "fold along x=655"
        #  - Split on the equals sign
        #  - line number = second entry
        #  - axis is last letter of the first entry
        fold_list = []

        for f in folds.strip().split('\n'):
            axis, line = f.split('=')
            fold_list.append({axis[-1] : int(line)})

        parts1_and_2(grid, fold_list, width, height)

if __name__ == "__main__":
    main()
