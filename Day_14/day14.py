#!/usr/bin/env python

import os
from collections import defaultdict

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


def analyse_chain(character_dict, pair_dict, rule_dict, steps):

    for step in range(1, steps + 1):
        new_dict = defaultdict(int)

        # (a,b) = the individual characters in the pair
        # count = the current count of this pair
        for pair, count in pair_dict.items():
            # print(f"pair {pair} : count {count}")

            # Get the new element to be inserted based on this pair
            # from the rules dictionary
            new_element = rule_dict[pair]
            # print(f"New element for {a+b} = {new_element}")

            # Create the two new pairs
            new_dict[pair[0] + new_element] += count
            new_dict[new_element + pair[1]] += count

            # print(f"{pair}:{count} -> {pair[0] + new_element} & {new_element + pair[1]}")

            # Add a counter for the new character
            character_dict[new_element] += count

        # print(f" After step {step} - new_dict = {new_dict}")
        # print(f" Counts = {character_dict}")
        pair_dict = new_dict

    print(f" After step {step} - new_dict = {new_dict}")
    print(f" Counts = {character_dict}")
    most_common = max(character_dict.values())
    least_common = min(character_dict.values())
    final = most_common - least_common

    print(f" Most common = {most_common} - Least common {least_common} - Final Value = {final}")


def part1(pair_dict, character_dict, rule_dict):
    print("Part 1:")

    analyse_chain(character_dict, pair_dict, rule_dict, 10)

    return


def part2(pair_dict, character_dict, rule_dict):
    print("Part 2:")

    analyse_chain(character_dict, pair_dict, rule_dict, 40)

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        # Load the different lines into different variables. First line is the template, followed
        # by a blank line and then the ruleset
        template = f.readline().strip()
        rules = f.read().strip().splitlines()

        # Split out our rules into a dictionary
        rule_dict = dict()

        # Loop through the rules, inserting it into a dictionary for the "pair to match : inserted element"
        for rule in rules:
            element_pair, insertion = rule.split(" -> ")
            rule_dict[element_pair] = insertion

        print(f"Rule Dict = {rule_dict}")

        # Create a couple of dictionaries to count our pairs, and also
        # count the individual letters.
        # The second dict is required as when we split "NNBC" to
        #   - NN
        #   - NB
        #   - BC
        # we only want to count 2 N's, not 3.
        pair_dict = defaultdict(int)
        character_dict = defaultdict(int)

        # Loop through the initial template counting each overlapping pair
        for a, b in zip(template, template[1:]):
            pair_dict[a + b] += 1

        # Loop through the initial template counting how many times each letter occurs
        for letter in template:
            character_dict[letter] += 1

        part1(pair_dict.copy(), character_dict.copy(), rule_dict)
        part2(pair_dict.copy(), character_dict.copy(), rule_dict)


if __name__ == "__main__":
    main()
