#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')

def part1(data):
    print("Part 1:")
    # print(data)
    # print(max(data))

    # Loop through aligning the crabs with each position and
    # keep track of fuel used
    lowest_fuel = -1
    best_alignment = -1

    for alignment in range(max(data)):
        # print(f"Align with {alignment}")

        # Rest the fuel counter for this alignment position
        fuel = 0

        for crab in data:
            # print(f"{crab} aligns {abs(crab - alignment)}")
            fuel += abs(crab - alignment)

        if fuel < lowest_fuel or lowest_fuel == -1:
            lowest_fuel = fuel
            best_alignment = alignment

    print(f"Part 1: Lowest fuel = {lowest_fuel} at alignment position {best_alignment}")

    return


# Pretty much the same as part one. We just need to do a different
# calculation for the fuel cost
def part2(data):
    print("Part 2:")

    # Loop through aligning the crabs with each position and
    # keep track of fuel used
    lowest_fuel = -1
    best_alignment = -1

    for alignment in range(max(data)):
        # print(f"\nAlign with {alignment}")

        # Rest the fuel counter for this alignment position
        fuel = 0

        for crab in data:
            # The new fuel cost is ( (delta * delta + 1 ) / 2)
            delta = int(abs(crab - alignment))
            fuel_cost = int((delta * (delta + 1) ) / 2)
            fuel += fuel_cost
            # print(f"{crab} delta {delta} - fuel {fuel_cost} ")

        if fuel < lowest_fuel or lowest_fuel == -1:
            lowest_fuel = fuel
            best_alignment = alignment

    print(f"Part 2: Lowest fuel = {lowest_fuel} at alignment position {best_alignment}")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        # Read the data in as integers
        data = [int(x) for x in f.readline().split(",")]

        part1(data)
        part2(data)


if __name__ == "__main__":
    main()
