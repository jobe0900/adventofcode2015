#!/usr/bin/env python3

import re
import operator

def Sue(children = None, 
        cats = None, 
        samoyeds = None, 
        pomeranians = None, 
        akitas = None, 
        vizslas = None, 
        goldfish = None, 
        trees = None, 
        cars = None, 
        perfumes = None):
    sue = dict()
    sue.setdefault("children", children)
    sue.setdefault("cats", cats)
    sue.setdefault("samoyeds", samoyeds)
    sue.setdefault("pomeranians", pomeranians)
    sue.setdefault("akitas", akitas)
    sue.setdefault("vizslas", vizslas)
    sue.setdefault("goldfish", goldfish)
    sue.setdefault("trees", trees)
    sue.setdefault("cars", cars)
    sue.setdefault("perfumes", perfumes)
    return sue

def first(lines):
    real_sue = Sue(3, 7, 2, 3, 0, 0, 5, 3, 2, 1)
    sues = parse_lines(lines)
    i = 1
    matches = []
    for sue in sues:
        valid = is_compatible_sue(sue, real_sue)
        if valid:
            matches.append(i)
            #print("Matching Sue nr {}".format(i))
        i += 1
    print("1. Matching Sues: {}".format(matches))

def second(lines):
    real_sue = Sue(3, 7, 2, 3, 0, 0, 5, 3, 2, 1)
    comparisons = Sue(
            children = operator.eq,
            cats = operator.gt,
            samoyeds = operator.eq,
            pomeranians = operator.lt,
            akitas = operator.eq,
            vizslas = operator.eq,
            goldfish = operator.lt,
            trees = operator.gt,
            cars = operator.eq,
            perfumes = operator.eq
            )
    sues = parse_lines(lines)
    i = 1
    matches = []
    for sue in sues[:]:
        valid = is_compatible_sue2(sue, real_sue, comparisons)
        if valid:
            matches.append(i)
            #print("Matching Sue nr {} ({})".format(i, sues[i-1]))
        i += 1
    print("2. Matching Sues: {}".format(matches))



def is_compatible_sue(sue, real_sue):
    for k in real_sue.keys():
        if sue[k] != None and sue[k] != real_sue[k]:
            return False
    return True


def is_compatible_sue2(sue, real_sue, comparisons):
    for k in real_sue.keys():
        if sue[k] == None:
            continue
        if not comparisons[k](sue[k], real_sue[k]):
            return False
    return True


def parse_lines(lines):
    sues = []
    for line in lines:
        sue = parse_line(line.strip())
        sues.append(sue)
    return sues


def parse_line(line):
    pattern = r"(\w+): (\d+)"
    matches = re.findall(pattern, line)
    sue = Sue()
    for m in matches:
        sue[m[0]] = int(m[1])
    return sue


if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
        first(lines)
        second(lines)
