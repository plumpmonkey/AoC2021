#!/usr/bin/env python

import os
import numpy as np

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


def flash(octopus, flashed, index):
    # print(f" Flashing {index}")

    # Check if this index has been flashed before, if so, abort
    if flashed[index[0]][index[1]] == True:
        print(f"    {index} - already flashed")
    else:
        # Set this index to have flashed and set its value to zero
        flashed[index[0]][index[1]] = True
        octopus[index[0]][index[1]] = 0

    # Determine width and height of the grid
    width = len(octopus[0])
    height = len(octopus)

    # Define our adjacent points (y,x) that we want to examine
    adjacent_points = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    # Loop through the adjacent points
    for direction in adjacent_points:
        delta_y, delta_x = direction

        new_y = index[0] + delta_y
        new_x = index[1] + delta_x

        # Check x and y boundary
        if (new_y in range(height) and new_x in range(width)):
            # Increment the new point if its not been flashed in this round
            if flashed[new_y][new_x] == False:
                octopus[new_y][new_x] += 1


def part1(octopus, flashed):
    print("Part 1:")

    # Counter to track number of flashes
    total_flashes = 0

    # Loop for the required number of steps
    for step in range(1,101):

        # Reset the flash map
        flashed = np.array(octopus < 0)

        # Add one to each element of the array
        octopus = octopus + 1

        while True:
            # Find the indicies which need to flash
            indices = np.argwhere(octopus > 9)

            # If no indexes need to be flashed, break out the loop
            if len(indices) == 0:
                break

            for index in indices:
                flash(octopus, flashed, index)

        # Count the number of flashes that happened
        print(f" Step - {step} - Flashed {np.count_nonzero(flashed == True)}")
        total_flashes += np.count_nonzero(flashed == True)

    print(f"Total Flashes - {total_flashes}")

    return


def part2(data):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        octopus = np.array([list(map(int, list(line.strip()))) for line in data])

        # Default an array to False for flash status
        flashed = np.array(octopus < 0)

        part1(octopus, flashed)
        #part2(data)


if __name__ == "__main__":
    main()
