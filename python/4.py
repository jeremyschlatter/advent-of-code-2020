def valid(s):
    m = [x.split(':')[0] for x in s.split()]
    return all(f in m for f in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

with open('4.txt') as f:
    print(sum(map(valid, f.read().split('\n\n'))))
