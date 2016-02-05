#!/usr/bin/env python3

ON = True
OFF = False
ON_C = '#'
OFF_C = '.'

def test():
    with open("testdata") as f:
        lines = f.readlines()
    grid = parse_lines(lines)
    print_grid(grid, ' ')

    steps = 4
    for i in range(steps):
        grid = step(grid)
        print_grid(grid, ' ')
    lights = count_lights_on(grid)
    print("Nr lights on: {}".format(lights))

def test2():
    with open("testdata") as f:
        lines = f.readlines()
    grid = parse_lines(lines)
    constant_lit_corners(grid)
    print_grid(grid, ' ')

    steps = 5
    for i in range(steps):
        grid = step(grid)
        constant_lit_corners(grid)
        print_grid(grid, ' ')
    lights = count_lights_on(grid)
    print("Nr lights on: {}".format(lights))


def first():
    with open("input") as f:
        lines = f.readlines()
    grid = parse_lines(lines)

    steps = 100
    for i in range(steps):
        grid = step(grid)
    lights = count_lights_on(grid)
    print("1. Nr lights on: {}".format(lights))


def second():
    with open("input") as f:
        lines = f.readlines()
    grid = parse_lines(lines)
    constant_lit_corners(grid)

    steps = 100
    for i in range(steps):
        grid = step(grid)
        constant_lit_corners(grid)
    lights = count_lights_on(grid)
    print("2. Nr lights on: {}".format(lights))


def constant_lit_corners(grid):
    size = len(grid)
    grid[0][0] = ON
    grid[0][size-1] = ON
    grid[size-1][0] = ON
    grid[size-1][size-1] = ON


def count_lights_on(grid):
    lights = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ON:
                lights += 1
    return lights


def parse_lines(lines):
    size = len(lines)
    grid = []
    x = y = 0
    for line in lines:
        grid.append(list((OFF,)*size))
        for c in line:
            if c == ON_C:
                grid[y][x] = ON
            x += 1
        y += 1
        x = 0
    return grid


def print_grid(grid, separator=''):
    print("\nGRID:")
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == ON:
                print(ON_C, end=separator)
            else:
                print(OFF_C, end=separator)
        print()


def step(grid):
    size = len(grid)
    next_grid = []
    for y in range(size):
        next_grid.append(list((OFF,) * size))
        for x in range(size):
            nr_neigh_on = count_lit_neighbours(x, y, grid)
            if (grid[y][x] == ON and nr_neigh_on in (2, 3)) or \
                    ((grid[y][x] == OFF) and (nr_neigh_on == 3)):
                next_grid[y][x] = ON
    return next_grid


def count_lit_neighbours(x, y, grid):
    size = len(grid)
    nr_lit = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if not (nx == x and ny == y) and grid[ny][nx] == ON:
                nr_lit += 1
    return nr_lit


if __name__ == "__main__":
    #test()
    #test2()
    first()
    second()
