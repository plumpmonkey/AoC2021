#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


def part1(data):
    print("Part 1:")

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
