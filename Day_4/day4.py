#!/usr/bin/env python

import os
from itertools import chain

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')

class BingoBoard(object):
    def __init__(self, rows, index):
        self.index = index;
        self.numbers = list(chain(*rows))
        self.boardDimension = len(rows[0])
        self.totalNumbers = len(self.numbers)
        self.Bingo = False


    # Receives the drawn numer and searches the board
    # for the number. If we find it, we replace the number
    # with an "X"
    def mark(self, number):
        for index, value in enumerate(self.numbers):
            # Check if number matches
            if self.Bingo:
                return False
            elif value == number:
                # Found the number, replace with an "X"
                self.numbers[index] = "X"
                # Check if we have won
                return (self.check_winner())
        return False


    # Checks if this board has a matching win condition
    def check_winner(self):
        # Check each row and column for win condition
        for i in range(self.boardDimension):
            #print(f"ROW {self.numbers[(self.boardDimension * i): (self.boardDimension * i) + self.boardDimension]}")
            #print(f"Column {self.numbers[i : self.totalNumbers : self.boardDimension]}")

            # Count the number of X's in each row and column
            row_count = self.numbers[(self.boardDimension * i): (self.boardDimension * i) + self.boardDimension].count("X")
            column_count = self.numbers[i : self.totalNumbers : self.boardDimension].count("X")

            if row_count == self.boardDimension or column_count == self.boardDimension:
                self.Bingo = True
                return self.calculate_score()


    def calculate_score(self):
        # Use list comprehension to filter out X's and sum the rest of the numbers
        return sum(x for x in self.numbers if x != "X" )



def part1(boards, drawn_numbers):
    print("Part 1:")

    # Loop through each drawn number
    for number in drawn_numbers:
        # Pass the number to each board
        for board in boards:
            # Mark the number off in the board.
            # Returns positive number if BINGO!
            if score := board.mark(number):
                print(f"Board Winner on Draw Num {number}- ID {board.index} - Score {score} - Remaining numbers {board.numbers}")
                print(f"Final Score = {number * score}")
                break
        else:
            continue
        break

    return


def part2(boards, drawn_numbers):
    print("Part 2:")

    numBoards = len(boards) - 1
    boardsFinished = 0

    # Loop through each drawn number
    for number in drawn_numbers:
        # Pass the number to each board
        for board in boards:
            # Mark the number off in the board.
            # Returns positive number if BINGO!
            # For Part 2, dont break out
            if score := board.mark(number):
                boardsFinished += 1
                if numBoards == boardsFinished :
                    print(f"  Board Winner on Draw Num {number}- ID {board.index} - Score {score} - Remaining numbers {board.numbers}")
                    print(f"  Final Score = {number * score}")


    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        # Read the first line in as our drawn number list
        drawn_numbers = [int(x) for x in f.readline().split(",")]

        # Read the remainder of the file as a list of lists (each row is a list)
        boardNumbers = [[int(x) for x in line.strip().split()] for line in f if line != "\n"]

        # Build the Bingo Boards. Pass in 5 rows at a time and create a list of boards
        boards = []
        for i in range (0, len(boardNumbers), 5):
            boards.append( BingoBoard(boardNumbers[i:i+5], int(i/5)) )

        part1(boards, drawn_numbers)
        part2(boards, drawn_numbers)


if __name__ == "__main__":
    main()
