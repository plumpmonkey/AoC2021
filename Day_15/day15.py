#!/usr/bin/env python

import os
import numpy as np

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


def part1(grid):
    print("Part 1:")

    height, width = grid.shape
    print(width,height)

    return


def part2(data):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()
        grid = np.array([list(map(int, row)) for row in data])

        part1(grid)

        #part2(data)


if __name__ == "__main__":
    main()
