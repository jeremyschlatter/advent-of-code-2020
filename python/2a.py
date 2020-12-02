from itertools import starmap

def parse(s):
    [r, c, pw] = s.split()
    return tuple(map(int, r.split('-'))), c[0], pw

def check(rng, c, pw):
    return int((n := pw.count(c)) >= rng[0] and n <= rng[1])

with open('2.txt') as f:
    print(sum(starmap(check, map(parse, f))))
