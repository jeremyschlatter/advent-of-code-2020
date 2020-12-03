with open('3.txt') as f:
    grid = [[c == '#' for c in l.strip()] for l in f]
    col = 0
    trees = 0
    for row in grid:
        if row[col]:
            trees += 1
        col += 3
        col %= len(row)
    print(trees)
