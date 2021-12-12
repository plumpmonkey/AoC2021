#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


def part1(adjacentDict):
    print("Part 1:")

    print(adjacentDict)

    paths = 0
    caves_to_vist = [('start')]
    visited_caves = []

    while caves_to_vist:
        cave = caves_to_vist.pop(0)
        if cave == 'end':
            print(f"Reached end via path {visited_caves}")
            paths += 1
            break
        else:
            if cave not in visited_caves:
                visited_caves.append(cave)

            for connection in adjacentDict[cave]:
                caves_to_vist.append(connection)

    return


def part2(data):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        # Create a dictionary of adjacent caves
        adjacentDict = dict()

        for line in data:
            cave1, cave2 = line.strip().split("-")

            # Set up the dictonary for cave1 -> cave2
            if cave1 in adjacentDict:
                adjacentDict[cave1].append(cave2)
            else:
                adjacentDict[cave1] = [cave2]

            # Also populate for cave2 -> cave1
            if cave2 in adjacentDict:
                adjacentDict[cave2].append((cave1))
            else:
                adjacentDict[cave2] = [cave1]


        part1(adjacentDict)


if __name__ == "__main__":
    main()
