#!/usr/bin/env python

import os
import numpy as np

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


def part1(grid, fold_list, width, height):
    print("Part 1:")

    for fold in fold_list:
        for axis, line in fold.items():
            print(f"Folding axis {axis} on line {line}")
            if axis == "y":



    return


def part2(data):
    print("Part 2:")

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
        width = max(dot_list[0]) + 1
        height = max(dot_list[1]) + 1

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

        part1(grid, fold_list, width, height)

if __name__ == "__main__":
    main()
