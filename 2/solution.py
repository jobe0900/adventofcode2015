#!/usr/bin/env python

def convert_string_array_to_numbers(arr):
    """Convert an array of strings to array of integers"""
    new_arr = []
    for e in arr:
        new_arr.append(int(e))
    return new_arr


def parse_line(line):
    dims = line.split("x")
    if len(dims) != 3:
        raise RuntimeError("Wrong dimensions of array")
    return convert_string_array_to_numbers(dims)


def smallest_in_array(arr):
    smallest = arr[0]
    for e in arr:
        if e < smallest:
            smallest = e

    return smallest


def calculate_area(dimensions_array):
    w = dimensions_array[0]
    h = dimensions_array[1]
    l = dimensions_array[2]

    lw_area = l*w
    wh_area = w*h
    hl_area = l*h

    extra_area = smallest_in_array([lw_area, wh_area, hl_area])
    surface_area = 2*(lw_area + wh_area + hl_area)

    return extra_area + surface_area


def find_shortest_perimeter(dims):
    dims = sorted(dims)
    return 2*(dims[0]+dims[1])


def calculate_volume(dims):
    return dims[0]*dims[1]*dims[2]


def test():
    arr = parse_line("2x3x4")
    print(arr)
    s = smallest_in_array([1,2,4,3,-2])
    print("smallest: {}".format(s))

    dim1 = [2,3,4]
    dim2 = [1,1,10]

    a = calculate_area(dim1)
    print("area of {0}: {1}".format(dim1, a))
    a = calculate_area(dim2)
    print("area of {0}: {1}".format(dim2, a))

    shortest = find_shortest_perimeter(dim1)
    print("shortest perimeter of {0}: {1}".format(dim1, shortest))
    v = calculate_volume(dim1)
    print("volume of {0}: {1}".format(dim1, v))
    shortest = find_shortest_perimeter(dim2)
    print("shortest perimeter of {0}: {1}".format(dim2, shortest))
    v = calculate_volume(dim2)
    print("volume of {0}: {1}".format(dim2, v))


def get_lines(f):
    lines = []
    for line in f:
        if len(line.strip()) > 0:
            lines.append(line)
    return lines


def get_dimensions(lines):
    dims = []
    for line in  lines:
        dims.append(parse_line(line))
    return dims


def first(dimensions):
    total_area = 0
    for dim in dimensions:
        area = calculate_area(dim)
        total_area += area
    print("1. Total area: {}".format(total_area))


def second(dimensions):
    total_length = 0
    for dim in dimensions:
        shortest = find_shortest_perimeter(dim)
        ribbon = calculate_volume(dim)
        total_length += shortest + ribbon
    print("2. Ribbon length: {}".format(total_length))


if __name__ == "__main__":
    #test()
    with open("input") as f:
        lines = get_lines(f)
        dimensions = get_dimensions(lines)
        first(dimensions)
        second(dimensions)
