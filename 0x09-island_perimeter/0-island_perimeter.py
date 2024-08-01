#!/usr/bin/python3

"""
Island Perimeter
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the given Island
    """
    count = 0
   
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1
    return count*2 + 2
