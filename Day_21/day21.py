#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


def part1(p1_start, p2_start):
    print("Part 1:")

    # Store player scores [player1, player2]
    # Players from here on in are now Player 0 and Player 1
    player_scores = [0,0]

    # Store current player position
    player_positions = [p1_start, p2_start]

    # Keep a track of which roll we are on
    roll_count = 0

    # Loop until we have a winner
    while max(player_scores) < 1000:
        # Determine which player is to go
        player_turn = roll_count % 2

        # Roll the dice.
        new_position, roll_count = roll_dice(player_positions[player_turn], roll_count)

        # Add the new position to the score
        player_scores[player_turn] += new_position

        # Update the new player position
        player_positions[player_turn] = new_position

    print(f"Final positions {player_positions}, Final scores {player_scores}, Roll Count {roll_count}")
    print(f"Calculation = {min(player_scores) * roll_count}")
    return


def roll_dice(player_position, roll_number):

    position = player_position

    # Roll the dice 3 times
    # the position increments
    for i in range(3):
        position += roll_number + 1 + i % 100

    # Set our new position back to a 1-10 number.
    # Hack in the poisition 0 = 10
    position = position % 10
    if position == 0:
        position = 10

    return  position, roll_number + 3

def part2(data):
    print("Part 2:")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        p1_start = int(data[0].split(" ")[-1])
        p2_start = int(data[1].split(" ")[-1])

        print(f"P1 {p1_start} P2 {p2_start}")

        part1(p1_start, p2_start)
        #part2(data)


if __name__ == "__main__":
    main()
