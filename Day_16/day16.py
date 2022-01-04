#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


def part1(data):
    print("Part 1:")

    data = "D2FE28"

    print(f"Input string - ", data[0])
    print("Length of data - ",len(data[0]))

    # Convert input string to hex

    intval = (int(data,16))

    # Convert hex to binary

    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=len(data[0]*8), type='b')
    
    print(f"Binary conversion - {format(intval, spec)}")

    return


def part2(data):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        part1(data)
        #part2(data)


if __name__ == "__main__":
    main()
