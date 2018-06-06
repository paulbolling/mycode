#!/usr/bin/env python3
simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]
def byAge(x):
    return x[1]
simpsonsAge = sorted(simpsons, key=byAge)
print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)