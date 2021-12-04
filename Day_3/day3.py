#!/usr/bin/env python

from collections import Counter
from collections import defaultdict

import os

import numpy
import numpy as np

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')

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

    print(f"  Ones-Count = {ones_count}")
    print(f"  Gamma = {int(gamma,2)}")
    print(f"  Epsilon = {int(epsilon, 2)}")
    print(f"  Power Consumption = {int(gamma,2) * int(epsilon, 2)}")

    return (int(gamma,2) * int(epsilon, 2))


def part2(data, numLines, numBits ):
    print("Part 2:")

    ## This time use NumPy to store the numbers
    num_list = np.array([list(i) for i in data], dtype=int)

    oxygen = analyse_list("oxygen", numBits, num_list)
    co2 = analyse_list("co2", numBits, num_list)
    life_support = oxygen * co2

    print(f"  LifeSupport = {life_support}")


    return


def analyse_list(mode, numBits, num_list):

    value = 0

    # Loop through the bits
    for i in range(numBits):
        # Debug code
        # print(f"Looking at Bit {i}")
        # print(num_list)
        # print(f"{i}: {num_list[:,i].sum()} - Len List = {len(num_list)}")

        # Check if this colum most common is a 1 or a 0
        if (num_list[:, i].sum()) >= len(num_list) / 2:
            # Most common is a 1
            # print(f"Index {i} is a 1")
            oneMostCommon = True
        else:
            # Most common is a zero
            # print(f"Index {i} is a 0")
            oneMostCommon = False

        temp_list = []

        # Loop through each line in the data and see if this
        # bit index matches the mostCommon value for this index
        for index, line in enumerate(num_list):
            if mode == "oxygen":
                if oneMostCommon == True and line[i] == 1:
                    temp_list.append(line)
                elif oneMostCommon == False and line[i] == 0:
                    temp_list.append(line)
            else:
                if oneMostCommon == True and line[i] == 0:
                    # Zero is least common
                    temp_list.append(line)
                elif oneMostCommon == False and line[i] == 1:
                    # One is least common
                    temp_list.append(line)


        # Replace our main list with the cut down list ready
        # for the next loop.
        num_list = np.array(temp_list)

        # Check if we have finished
        if (len(num_list) == 1):
            print("SUCCESS")

            value = int(str(''.join(num_list[0].astype(str))), 2)
            if mode == "oxygen":
                print(f"  Oxygen = {value}")
            else:
                print(f"  CO2 = {value}")
            break

    return value


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
