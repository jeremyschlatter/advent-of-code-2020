with open('1.txt') as f:
    s = set(map(int, f))
    print([d*r for d in s if (r := 2020-d) in s][0])
