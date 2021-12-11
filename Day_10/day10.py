#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
expected_values = {'(': ')', '[': ']', '{': '}', '<': '>'}


def part1(data):
    print("Part 1:")

    points = {')': 3, ']': 57, '}': 1197, '>': 25137}

    illegal_chars = []

    for index, line in enumerate(data):
        # Create a stack list where we can store all opening characters
        stack = []
        # print(f"\nLine = {line}")
        # Loop through each character in the line
        for char in line:

            # If its an opener, then add it to the stack
            if char in openers:
                stack.append(char)

            # Else, if it is a closer then check its the expected
            # closer for the last value (opener) on the stack
            elif char != expected_values[stack[-1]]:
                # print(f"Stack - {stack}")
                # print(f"  Line - {index + 1} - Expected {expected_values[stack[-1]]}, but found {char} instead")
                illegal_chars.append(char)
                break

            # Remove the last element on the list as the closer is an expected one
            else:
                del (stack[-1])

    # Loop through our illegal character array and calculate the points
    sum = 0
    for char in illegal_chars:
        sum += points[char]

    print(f"  Total score = {sum}")

    return


# Part 2 is very similar to Part 1 - I probably could have functionalised the main code.
def part2(data):
    print("Part 2:")

    points = {')': 1, ']': 2, '}': 3, '>': 4}

    scores = []

    for index, line in enumerate(data):

        score = 0

        # Create a stack list where we can store all opening characters
        stack = []
        corrupt = False

        # print(f"\nLine = {line}")
        # Loop through each character in the line
        for char in line:

            # If its an opener, then add it to the stack
            if char in openers:
                stack.append(char)

            # Else, if it is a closer then check its the expected
            # closer for the last value (opener) on the stack
            elif char != expected_values[stack[-1]]:
                # print(f"Stack - {stack}")
                # print(f"  Line - {index + 1} - Expected {expected_values[stack[-1]]}, but found {char} instead")
                corrupt = True
                break

            # Remove the last element on the list as the closer is an expected one
            else:
                del (stack[-1])

        if corrupt == False:
            # The line wasnt corrupt, so it must be incomplete
            for opener in reversed(stack):
                score = (score * 5) + int(points[expected_values[opener]])

            # print(f"  Score = {score}")
            scores.append(score)

    # All scores are in. Whats the scores Majory Doors?
    scores = sorted(scores)
    print(f"  Middle score = {scores[(int((len(scores) - 1 )/2))]}")


    return


def main():
    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        part1(data)
        part2(data)


if __name__ == "__main__":
    main()
