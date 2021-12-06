#!/usr/bin/env python
import os
import numpy as np
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)
input_file = os.path.join(dirname, 'input.txt')
#input_file = os.path.join(dirname, 'sample.txt')


# Function to expand coordinates based on the [x1,y1],[x2,y2] values
#
# If Part1 flag is set to TRUE, then the diagonal lines are ignored
def expand_coords(position, part1=True):
    # Break out the coords per line
    [[x1, y1], [x2, y2]] = position

    # Work out the delta
    x_delta = x2 - x1
    y_delta = y2 - y1

    line_coords = []

    # Work out which way the line is going and reorder to (min value, max value)
    if x_delta == 0:
        # Vertical line
        y1, y2 = min(y1, y2), max(y1, y2)

        # Get the coordinates of all points between the positions
        line_coords = ((x1, y) for y in range(y1, y2 + 1))

    elif y_delta == 0:
        # Horizontal line
        x1, x2 = min(x1, x2), max(x1, x2)

        # Get the coordinates of all points between the positions
        line_coords = ((x, y1) for x in range(x1, x2 + 1))

    else:
        # Diagonal line
        if part1 == True:
            pass
        else:
            x_increment = -1 if x_delta < 0 else 1
            y_increment = -1 if y_delta < 0 else 1

            line_coords = ((x, y) for x, y in zip(range(x1, x2 + x_increment, x_increment),
                                                  range(y1, y2 + y_increment, y_increment)))

    return line_coords


def part1(coords, dimensions):
    print("Part 1:")

    # Create a map
    map = np.zeros(dimensions, dtype=int)

    for position in coords:
        line_coords = expand_coords(position)

        # Update the map element for each line
        for pos in line_coords:
            map[pos] += 1

    print(f"Part 1: Number of overlaps = {str(np.count_nonzero(map >= 2))}")

    # Draw the map using matplotlib
    plt.imshow(map)
    plt.show()

    return


def part2(coords, dimensions):
    print("Part 2:")

    # Create a map
    map = np.zeros(dimensions, dtype=int)

    for position in coords:
        line_coords = expand_coords(position, part1=False)

        # Update the map element for each line
        for pos in line_coords:
            map[pos] += 1

    print(f"Part 2: Number of overlaps = {str(np.count_nonzero(map >= 2))}")

    # Draw the map using matplotlib
    plt.imshow(map)
    plt.show()

    return


def main():
    current_day = os.path.basename(__file__).split('.')[0]
    print(current_day)

    with open(input_file) as f:
        # Coords is an np array of lines containing a list of array [start[x,y], end[x,y]]
        coords = np.array([[([int(d) for d in c.split(",")]) for c in l.strip("\n").split(" -> ")] for l in f.readlines()])

        # Work out the map size
        dimensions = ((np.max(coords[:, :, 0] + 1), np.max(coords[:, :, 1] + 1)))
        print("Grid size = " + str(dimensions))

        part1(coords, dimensions)
        part2(coords, dimensions)


if __name__ == "__main__":
    main()
