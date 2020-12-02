from itertools import combinations

with open('1.txt') as f:
    for (a, b, c) in combinations(map(int, f), 3):
        if a + b + c == 2020:
            print(a * b * c)
