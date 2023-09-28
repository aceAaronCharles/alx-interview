#!/usr/bin/python3


def island_perimeter(grid):
    """
   A function that calculates the perimeter of a given island.
    """
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check left side
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right side
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
                # check top side
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check bottom side
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter
