#!/usr/bin/env python

def first(s):
    lefties = s.count("(")
    righties = s.count(")")
    level = lefties - righties
    print("1. level {0}".format(level))


def second(s):
    target = -1
    current = 0
    pos = 1
    for c in s:
        if c == "(":
            current += 1
        else:
            current -=1
        if current == target:
            break
        pos += 1
    print("2. reached level {0} in position {1}".format(target, pos))


if __name__ == "__main__":
    f = open("input")
    source = f.readline()
    first(source)
    second(source)
