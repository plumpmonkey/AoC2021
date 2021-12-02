#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

def part1(data):
    print("Part 1:")

    horizontal = 0;
    depth = 0;

    for line in data:
        instruction = line.split(' ')[0]
        amount = int(line.split(' ')[1])

        if instruction == "up":
            depth -= amount
        elif instruction == "down":
            depth += amount
        elif instruction == "forward":
            horizontal += amount

    print(f"Depth = {depth} - Horizonal = {horizontal} - Final = {depth * horizontal}")

    return (depth * horizontal)


def part2(data):
    print("Part 2:")

    horizontal = 0;
    depth = 0;
    aim = 0;

    for line in data:
        instruction = line.split(' ')[0]
        amount = int(line.split(' ')[1])

        if instruction == "up":
            aim -= amount
        elif instruction == "down":
            aim += amount
        elif instruction == "forward":
            depth += aim * amount
            horizontal += amount

    print(f"Depth = {depth} - Horizonal = {horizontal} - Final = {depth * horizontal}")

    return (depth * horizontal)


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        assert part1(data) == 1451208
        part2(data)


if __name__ == "__main__":
    main()
