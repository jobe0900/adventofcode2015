#!/usr/bin/env python3

import re


def operate_lights(grid, on_coord, off_coord, operation):
    for y in range(on_coord[0], off_coord[0]+1):
        for x in range(on_coord[1], off_coord[1]+1):
            if operation.endswith("on"):
                grid[y][x] = True
            elif operation.endswith("off"):
                grid[y][x] = False
            elif operation == "toggle":
                grid[y][x] = not grid[y][x]
            else:
                raise RuntimeError("Unknown operation: {}".format(operation))

def operate_lights_2(grid, on_coord, off_coord, operation):
    for y in range(on_coord[0], off_coord[0]+1):
        for x in range(on_coord[1], off_coord[1]+1):
            if operation.endswith("on"):
                grid[y][x] += 1
            elif operation.endswith("off"):
                if grid[y][x] > 0:
                    grid[y][x] -= 1
            elif operation == "toggle":
                grid[y][x] += 2 
            else:
                raise RuntimeError("Unknown operation: {}".format(operation))

def turn_on(grid, on_coord, off_coord):
    operate_lights(grid, on_coord, off_coord, "on")


def turn_off(grid, on_coord, off_coord):
    operate_lights(grid, on_coord, off_coord, "off")


def toggle(grid, on_coord, off_coord):
    operate_lights(grid, on_coord, off_coord, "toggle")

def count_lights(grid):
    lights = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]:
                lights += 1
    return lights

def calculate_brightness(grid):
    brightness = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            brightness += grid[y][x]
    return brightness

def init_grid(x,y):
    grid = [[False for i in range(x)] for j in range(y)]
    return grid

def init_grid_2(x,y):
    grid = [[0 for i in range(x)] for j in range(y)]
    return grid


def parse_line(line):
    """return tuple [on], [off], operation"""
    pattern = r"^(.+) (\d+),(\d+) .+ (\d+),(\d+)"
    match = re.match(pattern, line)
    on_coord = [int(match.group(2)), int(match.group(3))]
    off_coord = [int(match.group(4)), int(match.group(5))]
    operation = match.group(1)
    return (on_coord, off_coord, operation)


def first(f):
    grid = init_grid(1000, 1000)
    for line in f:
        tup = parse_line(line.strip())
        operate_lights(grid, tup[0], tup[1], tup[2])
    lights = count_lights(grid)

    print("1. Lit lights: {}".format(lights))


def second(f):
    grid = init_grid_2(1000, 1000)
    for line in f:
        tup = parse_line(line.strip())
        operate_lights_2(grid, tup[0], tup[1], tup[2])
    brightness = calculate_brightness(grid)

    print("2. Brightness: {}".format(brightness))


def test():
    g1 = init_grid(3,3)
    print("{} lights in {}".format(count_lights(g1), g1))
    turn_on(g1, [0,0], [1,1])
    print("{} lights in {}".format(count_lights(g1), g1))
    turn_off(g1, [1,1], [1,1])
    print("{} lights in {}".format(count_lights(g1), g1))
    toggle(g1, [0,0], [2,2])
    print("{} lights in {}".format(count_lights(g1), g1))

    x_sz = 1000
    y_sz = 1000
    g2 = init_grid(x_sz, y_sz)
    toggle(g2, [0,0], [999, 999])
    turn_off(g2, [499, 499], [500, 500])
    print("{} lights of {}".format(count_lights(g2), x_sz*y_sz))

    print(parse_line("turn on 489,959 through 759,964"))

    tup = parse_line("turn off 820,516 through 871,914")
    print(tup)

    tup = parse_line("toggle 756,965 through 812,992")
    print(tup, tup[0], tup[1], tup[2])

    g3 = init_grid_2(x_sz, y_sz)
    operate_lights_2(g3, [0,0], [0,0], "turn on")
    print("{} brightness".format(calculate_brightness(g3)))
    operate_lights_2(g3, [0,0], [999,999], "toggle")
    print("{} brightness".format(calculate_brightness(g3)))


if __name__ == "__main__":
    #test()
    with open("input") as f:
        first(f)
    with open("input") as f:
        second(f)
