#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def part1(data):
    print("Part 1:")

    count = 0
    lastNumber = int(data[0])

    for line in range(1,len(data)):
        if int(data[line]) > lastNumber:
            count += 1

        lastNumber = int(data[line])

    print(f"Total number of increases = {count}")

    return count


def part2(data):
    print("Part 2:")

    count = 0

    for line in range(3,len(data)):

        windowOneSum = int(data[line - 3]) + int(data[line - 2]) + int(data[line - 1])
        windowTwoSum = int(data[line - 2]) + int(data[line - 1]) + int(data[line])

        if(windowTwoSum > windowOneSum):
            count += 1

    print(f"Total number of increases = {count}")

    return count


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        assert part1(data) == 1766
        assert part2(data) == 1797


if __name__ == "__main__":
    main()
