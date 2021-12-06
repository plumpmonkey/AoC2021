#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
#inputfile = os.path.join(dirname, 'input.txt')
inputfile = os.path.join(dirname, 'sample.txt')


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

def part1(initial_list, days):
    print("Part 1:")

    Lanterns = []

    # Load initial state
    for index, timer in enumerate(initial_list):
        Lanterns.append( LanternFish(timer, index))

    # Loop through the specified days
    for x in range(1, days + 1):
        print(f"Day {x} - Number of Lanterns = {len(Lanterns)}")
        # for x in Lanterns:
        #     print(f"ID {x.ID} - Timer {x.timer}")

        newLanterns = []
        # Loop through each lantern
        for lantern in Lanterns:
            lantern.decrement()
            if(lantern.timer == 0):
                # print(f"ID {lantern.ID} spawning new lantern ID {len(Lanterns) + len(newLanterns)}")
                newLanterns.append(LanternFish(8, len(Lanterns) + len(newLanterns)))

        for x in newLanterns:
            Lanterns.append(x)

    for x in Lanterns:
        print(f"ID {x.ID} - Timer {x.timer}")
    print(f"Total Lanterns {len(Lanterns)}")

    return


def part2(initial_list, days):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        initial_list = [int(x) for x in f.readline().split(",")]

        part1(initial_list, days=18)
        #part2(data)


if __name__ == "__main__":
    main()
