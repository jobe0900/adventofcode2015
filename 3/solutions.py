#!/usr/bin/env python

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    def __repr__(self):
        return "Point({}, {})".format(self.x, self.y)
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.__repr__())


def get_new_point(point, direction):
    if direction == "^":
        return Point(point.x, point.y-1)
    elif direction == ">":
        return Point(point.x+1, point.y)
    elif direction == "<":
        return Point(point.x-1, point.y)
    elif direction == "v":
        return Point(point.x, point.y+1)
    else:
        raise RuntimeError("Unknown direction")


def first(line):
    p = Point(0,0)
    visited = {p}

    for direction in line.strip():
        p = get_new_point(p, direction)
        visited.add(p)
    
    print("1. Visited # of houses: {}".format(len(visited)))
    return len(visited)


def second(line):
    santa = Point(0,0)
    robosanta = Point(0,0)
    visited = {santa, robosanta}

    charpos = 0

    for direction in line.strip():
        if charpos % 2 == 0:
            santa = get_new_point(santa, direction)
            visited.add(santa)
        else:
            robosanta = get_new_point(robosanta, direction)
            visited.add(robosanta)
        charpos += 1

    print("2. Visited # of houses: {}".format(len(visited)))
    return len(visited)



def test():
    print(get_new_point(Point(0,0), "^"))
    print(get_new_point(Point(0,0), ">"))
    print(get_new_point(Point(0,0), "<"))
    print(get_new_point(Point(0,0), "v"))

    line = ">"
    print("{}: {}".format(line, first(line)))
    line = "^>v<"
    print("{}: {}".format(line, first(line)))
    line = "^v^v^v^v^v"
    print("{}: {}".format(line, first(line)))

    line = "^v"
    print("{}: {}".format(line, second(line)))
    line = "^>v<"
    print("{}: {}".format(line, second(line)))
    line = "^v^v^v^v^v"
    print("{}: {}".format(line, second(line)))


if __name__ == "__main__":
    #test()
    with open("input") as f:
        for line in f:
            first(line)
            second(line)
