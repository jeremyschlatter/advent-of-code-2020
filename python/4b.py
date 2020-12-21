def valid(s):
    f = dict(x.split(':') for x in s.split())
    try:
        return all([
            1920 <= int(f['byr']) <= 2002,
            2010 <= int(f['iyr']) <= 2020,
            2020 <= int(f['eyr']) <= 2030,
            {
                'cm': 150 <= (hgt:=int(f['hgt'][:-2])) <= 193,
                'in': 59 <= hgt <= 76,
            }[f['hgt'][-2:]],
            len(hcl:=f['hcl']) == 7 and hcl[0] == '#' and [int(c, 16) for c in hcl[1:]],
            f['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            len(f['pid']) == 9 and f['pid'].isdigit(),
        ])
    except:
        return False

with open('4.txt') as f:
    print(sum(map(valid, f.read().split('\n\n'))))
