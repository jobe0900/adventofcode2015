#!/usr/bin/env python3
import re

operations = [ "NOT", "AND", "OR", "LSHIFT", "RSHIFT" ]

def parse_line(line):
    """return a dict {wire: [input]}"""
    pattern = r"([\w\d]+)+ *([\w\d]+)? *([\w\d]+)? -> ([\w]+)"
    m = re.match(pattern, line)
    wire = None
    inp = list()
    if m:
        for i in range(1,4):
            if m.group(i):
                inp.append(m.group(i))
        wire = m.group(4)
        return {wire: inp}
    raise RuntimeError("Unknown pattern for line: {}".format(line))


def eval(input_list, symbols):
    val = None
    if isinstance(input_list, int):
        return input_list
    if len(input_list) == 1:
        if is_value(input_list[0]):
            val = int(input_list[0])
        elif is_symbol(input_list[0]):
            val = eval(symbols[input_list[0]], symbols)
            symbols[input_list[0]] = val
        else:
            raise RuntimeError("Invalid input (1 arg): {}".format(input_list))
    elif len(input_list) == 2:
        if input_list[0] == "NOT":
            val = ~ eval(input_list[1:], symbols)
        else:
            raise RuntimeError("Invalid input (2 args): {}".format(input_list))
    elif len(input_list) == 3:
        if input_list[1] in operations:
            val = eval_3(input_list, symbols)
        else:
            raise RuntimeError("Invalid input (3 args): {}".format(input_list))
    else:
        raise RuntimeError("Invalid input: {}".format(input_list))
    if is_value(val) and val < 0:
        val += 1 << 16
    return val


def eval_3(input_list, symbols):
    val = None
    if input_list[1] == "AND":
        val = eval(input_list[0:1], symbols) & eval(input_list[2:], symbols)
    elif input_list[1] == "OR":
        val = eval(input_list[0:1], symbols) | eval(input_list[2:], symbols)
    elif input_list[1] == "LSHIFT":
        val = eval(input_list[0:1], symbols) << eval(input_list[2:], symbols)
    elif input_list[1] == "RSHIFT":
        val = eval(input_list[0:1], symbols) >> eval(input_list[2:], symbols)
    else:
        raise RuntimeError("Invalid input: {}".format(input_list))
    return val


def is_value(sym):
    if isinstance(sym, int):
        return True
    if isinstance(sym[0], int):
        return True
    return sym[0].isdigit()


def is_symbol(sym):
    if (sym not in operations) and (not sym.isdigit()):
        return True
    return False



def test():
    print(parse_line("123 -> x"))
    print(parse_line("NOT y -> x"))
    print(parse_line("x AND y -> x"))
    print(parse_line("123 OR 456 -> a"))

    x = "3"
    print("{} of type {}, is val: {}, is symbol: {}, type: {}".format(x, type(x), is_value(x), is_symbol(x), type(x)))
    x = "a"
    print("{} of type {}, is val: {}, is symbol: {}, type: {}".format(x, type(x), is_value(x), is_symbol(x), type(x)))
    x = "AND"
    print("{} of type {}, is val: {}, is symbol: {}, type: {}".format(x, type(x), is_value(x), is_symbol(x), type(x)))

    l1 = "123 -> x"
    symbols = dict()
    p1 = parse_line(l1)
    v1 = eval(p1["x"], symbols)
    print("{} eval {}".format(l1, v1))


def first(f, wire):
    symbols = dict()
    for line in f:
        d = parse_line(line)
        symbols.update(d)
    val = eval(wire, symbols)
    print("1. value on wire {}: {}".format(wire, val))
    return val

def second(f, wire):
    b_val = first(f, "a")
    f.seek(0)
    symbols = dict()
    for line in f:
        d = parse_line(line)
        symbols.update(d)
    symbols["b"] = b_val
    val = eval(wire, symbols)
    print("2. value on wire {}: {}".format(wire, val))
    return val


if __name__ =="__main__":
    #test()
    with open("input") as f:
        first(f, "a")
    with open("input") as f:
        second(f, "a")
