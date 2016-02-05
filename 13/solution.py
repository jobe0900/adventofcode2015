#!/usr/bin/env python3

from itertools import permutations

def first(lines):
    happiness = parse_lines(lines)
    #print("happiness: {}".format(happiness))
    perm = permutations(happiness.keys())
    max_happiness = 0
    best_seating = None
    for p in perm:
        #print("permutation: {}".format(p))
        happ = evaluate_happiness(p, happiness)
        if happ > max_happiness:
            max_happiness = happ
            best_seating = p

    return best_seating, max_happiness



def second(lines):
    happiness = parse_lines(lines)
    add_myself(happiness, "Myself", 0)
    perm = permutations(happiness.keys())
    max_happiness = 0
    best_seating = None
    for p in perm:
        happ = evaluate_happiness(p, happiness)
        if happ > max_happiness:
            max_happiness = happ
            best_seating = p

    return best_seating, max_happiness


def add_myself(happiness, name, val):
    happiness.setdefault("Myself", dict())
    for pers in happiness.keys():
        if pers != name:
            happiness[pers].update({name:val})
            happiness[name].update({pers:val})


def evaluate_happiness(perm, happiness):
    total = 0
    for i in range(-1, len(perm)-1):
        p = perm[i]
        n = perm[i+1]
        h1 = happiness[p][n]
        h2 = happiness[n][p]
        total += h1
        total += h2
        #print("    Evaluate {}: {} <-> {} :  {} <-> {} (total: {})".format(perm, p, n, h1, h2, total))
    return total


def parse_lines(lines):
    """create dict {person: {neighbour: happiness}}"""
    happiness = dict()
    for line in lines:
        pers, neigh, points = parse_line(line.strip())
        happiness.setdefault(pers, dict()).update({neigh:points})
    return happiness


def parse_line(line):
    words = line.split()
    pers = words[0]
    plusminus = words[2]
    points = int(words[3])
    neigh = words[-1].strip('.')

    if plusminus == "lose":
        points = points * -1
    return pers, neigh, points

if __name__ == "__main__":
    #with open("testdata") as f:
    with open("input") as f:
        lines = f.readlines()
    best_seating1, max_happiness1 = first(lines)
    print("1. Max happiness {} : {}".format(best_seating1, max_happiness1))
    best_seating2, max_happiness2 = second(lines)
    print("2. Max happiness {} : {}".format(best_seating2, max_happiness2))
    print("2. DIFFERENCE: {}".format(max_happiness2 - max_happiness1))


