#!/usr/bin/env python3

import itertools
import bisect


def test():
    #lower_bound = 130
    house_nr, delivered = sol1(lower_bound)
    print("House {} got {} presents (> {})".format(house_nr, delivered, lower_bound))

def first():
    #lower_bound = 130
    lower_bound = 29000000
    house_nr, delivered = sol1(lower_bound)
    print("1. House {} got {} presents (> {})".format(house_nr, delivered, lower_bound))

def second():
    #lower_bound = 130
    lower_bound = 29000000
    house_nr, delivered = sol2(lower_bound)
    print("2. House {} got {} presents (> {})".format(house_nr, delivered, lower_bound))

# from reddit leader solution algorithm 1
def sol1(target):
    packages_per_house = 10
    target_house = target // packages_per_house
    houses = [0] * (target_house)
    for i in range(1, target_house):
        for j in range(i, target_house, i):
            houses[j] += i*packages_per_house
    houses = list(itertools.takewhile(lambda x: x != 0, houses[1:]))
    #print(houses)
    house = 0
    smallest = max(houses)
    for nr in range(len(houses)):
        if houses[nr] >= target and houses[nr] < smallest:
            smallest = houses[nr]
            house = nr
            break   # when encoutering the first match
    house += 1
    return house, smallest

# based on sol1
def sol2(target):
    max_house_per_elf = 50
    packages_per_house = 11
    target_house = target // packages_per_house
    houses = [0] * (target_house)
    for i in range(1, target_house):
        delivered_to_nr_houses = 0
        for j in range(i, target_house, i):
            if delivered_to_nr_houses >= max_house_per_elf:
                break
            houses[j] += i*packages_per_house
            delivered_to_nr_houses += 1
    houses = list(itertools.takewhile(lambda x: x != 0, houses[1:]))
    #print(houses)
    house = 0
    smallest = max(houses)
    for nr in range(len(houses)):
        if houses[nr] >= target and houses[nr] < smallest:
            smallest = houses[nr]
            house = nr
            break   # when encoutering the first match
    house += 1
    return house, smallest


def binary_search_at_least(target, low, high):
    found = False
    while not found:
        mid = (low + high) // 2
        if mid == low or mid == high:
            print("  Low {} < Mid {} (delivered: {}) < High {}".format(low, mid, deliver(mid), high))
            return high, deliver(high)
        mid_deliver = deliver(mid)
        if mid_deliver == target:
            return mid, target
        if mid_deliver < target:
           low = mid
        elif mid_deliver > target:
            high = mid

def deliver(house):
    delivered = 0
    packages_per_house = 10
    for elf in range(1, house+1):
        if house % elf == 0:
            delivered += elf * packages_per_house
    return delivered

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)

def func_find(lower_bound):
    found = list(itertools.takewhile(lambda x: x < lower_bound, map(deliver, itertools.count(1))))
    house = len(found) + 1 # the nex house gets the package
    #for i in found:
        #house += 1
    return house



def find_lowest_housenr(lower_bound):
    house = 0
    delivered = 0
    packages_per_house = 10

    while delivered < lower_bound:
        delivered = 0
        house += 1
        for elf in range(1, house+1):
            if house % elf == 0:
                delivered += elf * packages_per_house
                #print("  House {}, elf {}, delivered {}".format(house, elf, delivered))
        #print("House {} got {} presents".format(house, delivered))
    return house, delivered


if __name__ == "__main__":
    #test()
    first()
    second()
