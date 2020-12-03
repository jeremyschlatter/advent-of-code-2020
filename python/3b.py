from lib import *

with open('3.txt') as f:
    grid = [[c == '#' for c in l.strip()] for l in f]

def collisions(dx, dy):
    col = 0
    trees = 0
    for row in range(0, len(grid), dy):
        if grid[row][col]:
            trees += 1
        col += dx
        col %= len(grid[row])
    return trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(product(starmap(collisions, slopes)))
