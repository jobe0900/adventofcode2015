#!/usr/bin/env python3

import itertools

# rows are generated with accumulate, starting with line_nr first in seq [col, col+1...]
# cols are genereated with an extra col_nr first in seq [col, 1, 2, 3]


def first():
    x = 3083
    y = 2978
    nr = calc_order(x, y)
    #print("Order nr for row {}, col {} = {}".format(x, y, nr))

    code = 20151125
    for i in range(1, nr):
        code = calc_next_code(code)
    print("1. The code is {} (for (row, col) = ({}, {}, ordernr {}))".format(code, x, y, nr))


def calc_next_code(current):
    return (current * 252533) % 33554393


def calc_order(col, row):
    acc = itertools.accumulate(itertools.chain([col], itertools.count(1)))
    l = itertools.islice(acc, col-1, None)
    nr = itertools.islice(l, row-1, row)
    return int(list(nr)[0])


if __name__ == "__main__":
    first()
