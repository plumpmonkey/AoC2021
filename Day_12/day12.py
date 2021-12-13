#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample-3.txt')

paths = 0


# Walk through the cave map in a recursive fashion.
# We seem to need to take a copy of the visited caves list to pass into
# the recursive function as Python seems to have visibility scope of these
# variables in the recursive function and this caused no end of issues....
def explore_cave(cave, visited_caves, adjacentDict, part2=False, visited_small_cave_twice=False):

    global paths

    visited_copy= visited_caves.copy()

    visited_copy.append(cave)
    # print(f"cave = {cave} visited {visited_caves}")

    if cave == 'end':
        # print(f"Reached end via path {visited_copy}")
        paths += 1
        return
    else:

        # Part 1 logic is that we can only visit lower case caves once
        if part2 == False:
            for connection in adjacentDict[cave]:
                if connection.islower() and (connection != "start") and connection not in visited_caves:
                    # print(f"Adding lower case cave {connection}")
                    explore_cave(connection, visited_copy, adjacentDict)
                elif connection.isupper():
                    # print(f"Adding uppercase cave {connection}")
                    explore_cave(connection, visited_copy, adjacentDict)

        # Part 2 logic is that we can visit ONE lower case cave twice. Pass through a boolean
        # detailing if we enter a lower cave for the second time.
        # Once this is set, we cant add a lower case cave thats in the visited list again.
        # Otherwise the logic is the same as before.
        else:
            for connection in adjacentDict[cave]:
                if connection.islower() and (connection != "start"):
                    if (connection not in visited_caves):
                        explore_cave(connection, visited_copy, adjacentDict, part2=True, visited_small_cave_twice=visited_small_cave_twice)
                    elif (connection in visited_caves) and (visited_small_cave_twice == False):
                        explore_cave(connection, visited_copy, adjacentDict, part2=True, visited_small_cave_twice=True)

                # Upper case cave. Just add it.
                elif connection.isupper():
                    explore_cave(connection, visited_copy, adjacentDict, part2=True, visited_small_cave_twice=visited_small_cave_twice)

def part1(adjacentDict):
    print("Part 1:")

    print(adjacentDict)

    visited_caves = []

    explore_cave('start', visited_caves, adjacentDict)

    print(f"Part 1: Number of Paths = {paths}")
    return


def part2(adjacentDict):
    print("Part 2:")

    visited_caves = []

    explore_cave('start', visited_caves, adjacentDict, part2=True)

    print(f"Part 2: Number of Paths = {paths}")
    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        # Create a dictionary of adjacent caves
        adjacentDict = dict()

        for line in data:
            cave1, cave2 = line.split("-")

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
        part2(adjacentDict)


if __name__ == "__main__":
    main()
