#!/usr/bin/env python

import os
from collections import Counter, defaultdict

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


class LanternFish(object):
    def __init__(self, initial_timer, ID):
        self.timer = initial_timer
        self.ID = ID

    def decrement(self):
        if (self.timer == 0):
            self.timer = 6
        else:
            self.timer -= 1
            return


# Part one uses a very inefficiant method to model each Lantern Fish
# This is very resource intensive and totally unsuitable for Part 2.
# .... I really wish they would show you part 2 before you get too far in.....
def part1(initial_list, days):
    print("Part 1:")

    Lanterns = []

    # Load initial state
    for index, timer in enumerate(initial_list):
        Lanterns.append( LanternFish(timer, index))

    # Print initial state
    # temp = []
    # for lantern in Lanterns:
    #     temp.append(lantern.timer)
    # print(temp)

    # Loop through the specified days
    for x in range(1, days + 1):

        newLanterns = []
        # Loop through each lantern
        for lantern in Lanterns:
            if(lantern.timer == 0):
                # print(f"ID {lantern.ID} spawning new lantern ID {len(Lanterns) + len(newLanterns)}")
                newLanterns.append(LanternFish(8, len(Lanterns) + len(newLanterns)))

            # Decrement each counter
            lantern.decrement()

        # After we have been through all lanterns, add any new ones to the list
        for newLantern in newLanterns:
            Lanterns.append(newLantern)

        # Print end of day state
        # temp = []
        # for lantern in Lanterns:
        #     temp.append(lantern.timer)
        # print (temp)

        print(f"Day {x} - Number of Lanterns = {len(Lanterns)}")

    for x in Lanterns:
        pass
        # print(f"ID {x.ID} - Timer {x.timer}")
    print(f"Total Lanterns {len(Lanterns)}")

    return


# A much quicker and less resource intensive solution that uses
# Python counters and dictionary to keep track of the number of
# fish at each timer value.
# Should have thought of this first tbh......
def part2(initial_list, days):
    print("Part 2:")

    # Get the initial list into a counter
    counts = Counter(initial_list)

    for day in range(days + 1):
        print(f"Day {day} - Number of Lanterns = {sum(counts.values())}")
        fishDict = defaultdict(int)

        # Sort the counter list so we decrement the
        # lowest value fish first
        for timer, count in sorted(counts.items()):
            # print(f"Timer = {timer} - count {count}")
            if timer == 0:
                # If the timer == 0, add this number of
                # lantern fish to the count of fish with a
                # timer of 6 (resetting the fish timer)
                #
                # Create the same amount of fish with an initial
                # timer of 8. (create new fish)
                fishDict[6] += count
                fishDict[8] = count
            else:
                # Otherwise, decrement the timer value
                fishDict[timer -1 ] += count

        # Now have a dict with the new counts. Copy this back to
        # the Counter object
        # print(fishDict)
        counts = fishDict

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        initial_list = [int(x) for x in f.readline().split(",")]

        part1(initial_list, 80)
        part2(initial_list, 256)

if __name__ == "__main__":
    main()
