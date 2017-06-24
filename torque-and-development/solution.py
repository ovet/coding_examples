#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    connected = {}
    n, m, x, y = input().strip().split(' ')
    n, m, x, y = [int(n), int(m), int(x), int(y)]
    for a1 in range(m):
        city_1, city_2 = input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        
        if city_1 in connected and city_2 not in connected[city_1]:
            connected[city_1].append(city_2)

        if city_2 in connected and city_1 not in connected[city_2]:
            connected[city_2].append(city_1)

        if city_1 not in connected and city_2 not in connected:
            connected[city_1] = [city_2]

    temp_dict = connected.copy()
    
    for name, values in temp_dict.items():
        if name in connected:
            for v in values:
                if v in connected and v is not name:
                    connected[name].extend(connected[v])
                    del connected[v]

    for name, values in connected.items():
        connected[name] = list(set(values))
        if name in values:
            connected[name].remove(name)

    sum = 0
    total_cities = 0
    for array in connected.values():
        total_cities += len(array)+1
        if x > y:
            sum += x+(y*(len(array)))
        else:
            sum += x*(len(array)+1)

    if n > total_cities:
        sum += x*(n - total_cities)

    print(sum)