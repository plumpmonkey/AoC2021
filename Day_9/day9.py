#!/usr/bin/env python

import os
import numpy as np

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')
#inputfile = os.path.join(dirname, 'sample.txt')


# Function to get a list of all adjacent coordinates from a starting location
def find_adjacent_coords(start_y, start_x, height, width):

    # Define our adjacent points (y,x) that we want to examine
    adjacent_points = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    adjacent_coords = []

    # Loop through the adjacent points
    for direction in adjacent_points:
        delta_y, delta_x = direction

        # Check x and y boundry
        if (start_y + delta_y in range(height) and start_x + delta_x in range(width)):
            # print(f"Point [{start_y + delta_y}][{start_x + delta_x}] is adjacent to [{start_y}][{start_x}]")
            adjacent_coords.append([start_y + delta_y,start_x + delta_x])

    return adjacent_coords

def find_lowest_locations(data, height, width):
    # Create a list to store our found low points
    low_points = []

    # Default a list that contains the coordinates for the lowest location
    lowest_point_locations = []

    for y in range(height):
        for x in range(width):
            location = data[y][x]

            # Default our location to be the lowest point
            # We will examine each adjacent location and set this
            # to FALSE if an adjacent point is lower than us.
            is_lowest = True

            # Find all the adjacent coordinates to this location
            adjacent_coords = find_adjacent_coords(y, x, height, width)

            # Loop through all adjacent points and determine its value
            for coord in adjacent_coords:
                adjacent_location = data[coord[0]][coord[1]]

                # If an adjacent point is lower than us, change our status to not the lowest
                if adjacent_location <= location:
                    is_lowest = False
                    break;

            # If we are the lowest point after searching all adjacent points, then store the location
            if is_lowest:
                lowest_point_locations.append([y, x])

    return lowest_point_locations


def part1(data, height, width):
    print("Part 1:")

    # Get list of coordinates of all lowest points
    lowest_point_locations = find_lowest_locations(data, height, width)

    # We now have a list of our lowest points
    #print(lowest_point_locations)

    # Default the risk value
    risk_value = 0

    # Loop through lowest points and adjust risk value
    for location in lowest_point_locations:
        # print(f"Value {data[location[0]][location[1]]} at location {location[0]}, {location[1]} is lowest")
        risk_value += (data[location[0]][location[1]]) + 1

    print(f"  Final Risk Value = {risk_value}")


def part2(data, height, width):
    print("Part 2:")

    lowest_point_locations = find_lowest_locations(data, height, width)
    # print(f"Lowest points - {lowest_point_locations}")

    # Default our basin size list
    basins = []

    # Loop through each lowest point and work out its basin
    for start_point in lowest_point_locations:

        # print(f"Start Point = {start_point}")

        visited_locations = []
        locations_to_visit = [start_point]

        # Keep going whilst we have locations to look at
        while len(locations_to_visit) > 0:
            # Remove the location from the "to_visit" list and append it to the "visited" list
            location = locations_to_visit.pop(0)
            # print(f"Visiting {location}")
            visited_locations.append(location)

            # Coordinates of the current location
            y,x = location

            # Find all adjacent points to this location
            adjacent_locations = find_adjacent_coords(y, x, height, width)
            # print(f" Location {location} - adjacents {adjacent_locations}")

            # Loop through each adjacent location
            for location in adjacent_locations:
                # If the value of the adjacent location is not 9, and it is a new location, then we must visit it.
                if (data[location[0]][location[1]] < 9) \
                    and location not in visited_locations \
                    and location not in locations_to_visit:

                    # print(f" Adding {location} to the 'to be visited' list")
                    locations_to_visit.append(location)

        # print(f"\n Visited {visited_locations}")
        # print(f" Basin Size = {len(visited_locations)}\n")
        basins.append(len(visited_locations))

    # Sort the basin list and get the last 3 (largest)
    # Use numpy.prod() to multiply the list
    print(f" Basin product: {np.prod((sorted(basins)[-3:]))}")

    return


def main():

    currentDay = os.path.basename(__file__).split('.')[0]
    print(currentDay)

    with open(inputfile) as f:
        data = f.read().splitlines()

        # Convert the data into a list array of each digit.
        # (Since map() returns an iterator (a map object), you need call list()
        # so that you can exhaust the iterator and turn it into a list object.)
        data2 = [list(map(int, list(line.strip()))) for line in data]

        # Convert the input data to a numpy array
        data = np.array(data2, dtype=int)

        # Determine the size of the input grid
        height, width = data.shape

        # print(height, width)
        # print(data)

        part1(data, height, width)
        part2(data, height, width)


if __name__ == "__main__":
    main()
