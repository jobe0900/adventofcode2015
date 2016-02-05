#!/usr/bin/env python3

import itertools

def test():
    target = 25
    with open("testdata") as f:
        lines = f.readlines()
    containers = parse_lines(lines)
    print("Containers: {}".format(containers))
    combs = find_combinations(containers, target)
    print("FOUND combinations:")
    for c in combs:
        print("    {}".format(c))

def first(lines):
    target = 150
    containers = parse_lines(lines)
    combs = find_combinations(containers, target)
    print("1. Found {} combinations".format(len(combs)))
    return combs

def second(lines):
    target = 150
    containers = parse_lines(lines)
    combs = find_combinations(containers, target)
    min_nr_bottles = find_min_nr_bottles_in_combination(combs)
    nr_combs_with_min = find_nr_minimal_combinations(min_nr_bottles, combs)
    print("2. {} combinations with {} number of bottles".format(nr_combs_with_min, min_nr_bottles))

def find_min_nr_bottles_in_combination(combs):
    min_nr_bottles = float('Inf')
    for c in combs:
        if len(c) < min_nr_bottles:
            min_nr_bottles = len(c)
    return min_nr_bottles

def find_nr_minimal_combinations(min_nr_bottles, combs):
    nr_combs_with_min = 0
    for c in combs:
        if len(c) == min_nr_bottles:
            nr_combs_with_min += 1
    return nr_combs_with_min

def find_combinations(containers, target):
    combs = []
    for i in range(len(containers)):
        for comb in itertools.combinations(containers, i):
            if sum(comb) == target:
                combs.append(comb)
    return combs

def parse_lines(lines):
    c = []
    for line in lines:
        c.append(int(line.strip()))
    return c


if __name__ == "__main__":
    #test()
    with open("input") as f:
        lines = f.readlines()
        first(lines)
        second(lines)
