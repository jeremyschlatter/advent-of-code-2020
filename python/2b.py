from itertools import starmap

def parse(s):
    [r, c, pw] = s.split()
    return tuple(map(int, r.split('-'))), c[0], pw

def check(ixs, c, pw):
    return int((pw[ixs[0]-1] == c) != (pw[ixs[1]-1] == c))

with open('2.txt') as f:
    print(sum(starmap(check, map(parse, f))))
