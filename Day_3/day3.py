#!/usr/bin/env python

from collections import Counter
from collections import defaultdict

import os

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')

def part1(data, numLines, numBits):
    print("Part 1:")

    # Default the dictionary entries in order
    ones_count = {}
    for index, value in enumerate(data[0]):
        ones_count[index] = 0

    # Loop through the data counting the ones
    for line in data:
        for index, value in enumerate(line):
           if value == '1':
                ones_count[index] += 1

    gamma = ""
    epsilon = ""
    # Loop through our counted bit
    for index in ones_count:
            # If the nuber of ones is more then half the length of the data, then the
            # most common bit in this index is a `1`
            if ones_count[index] > numLines / 2:
                gamma += str(1)
                epsilon += str(0)
            else:
                # 0 is the most common bit.
                gamma += str(0)
                epsilon += str(1)

    print(f"  Gamma = {int(gamma,2)}")
    print(f"  Epsilon = {int(epsilon, 2)}")
    print(f"  Power Consumption = {int(gamma,2) * int(epsilon, 2)}")

    return (int(gamma,2) * int(epsilon, 2))


def part2(data, numLines, numBits ):
    print("Part 2:")

    # Default the dictionary entries in order
    ones_count = {}
    for index, value in enumerate(data[0]):
        ones_count[index] = 0

    # Loop through the data counting the ones
    for line in data:
        for index, value in enumerate(line):
           if value == '1':
                ones_count[index] += 1

    # Take a copy of our data.
    oxygen_data = data

    # Check we have more than one entry left in our data
    #if(len(oxygen_data) > 1):

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        numLines = len(data)
        numBits = len(data[0])

        print(f"Number of lines in data {numLines}")
        print(f"Length of a line {numBits} bits")

        part1(data, numLines, numBits)
        part2(data, numLines, numBits)


if __name__ == "__main__":
    main()
