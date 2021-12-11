#!/usr/bin/env python

import os
import itertools
from collections import defaultdict

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


def part1(signals, output):
    print("Part 1:")

    sum = 0

    # Loop through the input signals
    for line in output:
        line_sum = 0
        # Loop through each input digit
        for digit in line:
            # Check the length of the digit.
            # Digit 1 = Length 2
            # Digit 4 = Length 4
            # Digit 7 = Length 3
            # Digit 8 = Length 7
            if len(digit) in (2, 4, 3, 7):
                line_sum += 1
                sum += 1

    print(f"  Part 1: Total of Digits 1, 4, 7 & 8 = {sum}")
    return


def part2(signals, output):
    print("Part 2:")

    # Digit patterns
    # 2 segments = 1
    # 3 segments = 7
    # 4 segments = 4
    # 5 segments = 2, 3, 5
    # 6 segments = 0, 6, 9
    # 7 segments = 8

    # Default our final output sum
    output_value_sum = 0

    # Loop through each line of input signals
    for line_num, input_signal in enumerate(signals):
        # Store our signals via length in a dictionary
        numberDict = defaultdict(list)

        for x in input_signal:
            numberDict[len(x)].append(set(x))

        # Create an empty list  to store our number sets for each digit
        numberMap: list[[]] = [None for _ in range (10)]

        # Sort the list in length order.
        line = sorted(input_signal, key=len)

        # Find the easy numbers first (1, 7, 4 & 8)
        for number in line:
            if len(number) == 2:
                # Digit 1 == 2 segments
                numberMap[1] = number
            elif len(number) == 3:
                # Digit 7 = 3 segments
                numberMap[7] = number
            elif len(number) == 4:
                # Digit 4 = 4 segments
                numberMap[4] = number
            elif len(number) == 7:
                # Digit 8 = 7 segments segments
                numberMap[8] = number

        # Second pass - Use some set theory to work out the other numbers
        for number in line:
            if len(number) == 5:
                # 5 segments could be Digits 2, 3 or 5
                #
                # Digit 1 is a subset of Digit 3 and no others.
                # if numberMap[1].issubset(number):
                #     numberMap[3] = number
                if (set(numberMap[1])).issubset(number):
                    numberMap[3] = number

                # Digit 4 is a subset of Digit 5 + Digit 1 (Digit 2 is not)
                elif(set(numberMap[4]).issubset(set(number).union(numberMap[1]))):
                    numberMap[5] = number
                else:
                    # Therefore, the remaining possibility is this has to be
                    # Digit 2
                    numberMap[2] = number

            elif len(number) == 6:
                # 6 segments could be Digits 0, 6 or 9
                #
                # Digit 1 is NOT a subset of Digit 6 (but is for 0 and 9)
                if not (set(numberMap[1]).issubset(set(number))):
                    numberMap[6] = number

                # Digit 4 is a subset of 9, but not 0
                elif(set(numberMap[4]).issubset(set(number))):
                    numberMap[9] = number
                else:
                    # Therefore the remaining possibility is this has to be
                    # Digit 0
                    numberMap[0] = number

        # At this point we have a number map with the signals in digit order.
        # Now read the output, and work out what the numbers are.
        digits = ""
        for i,v in enumerate(output[line_num]):
            for j, v2 in enumerate(numberMap):
                if(set(v2) == set(v)):
                    digits += str(j)

        output_value_sum += int(digits)

    print(f"  Final value = {output_value_sum}")
    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        signals = [x.split('|')[0].strip().split(' ') for x in data]
        output = [x.split('|')[1].strip().split(' ') for x in data]

        part1(signals, output)
        part2(signals, output)


if __name__ == "__main__":
    main()
