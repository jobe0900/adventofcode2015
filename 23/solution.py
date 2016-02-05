#!/usr/bin/env python3

import re

REGISTERS = {}
INSTRUCTIONS = {}
PROGRAM = []


def first():
    with open("input") as f:
        lines = f.readlines()
    program = load(lines)
    init()
    run(program)
    print("1. Registers: {}".format(REGISTERS))


def second():
    with open("input") as f:
        lines = f.readlines()
    program = load(lines)
    init(a=1, b=0)
    run(program)
    print("2. Registers: {}".format(REGISTERS))


def init(a=0, b=0):
    init_registers(a,b)
    init_instrcutions()


def init_registers(a=0,b=0):
    REGISTERS.setdefault("a", a)
    REGISTERS["a"] = a
    REGISTERS.setdefault("b", b)
    REGISTERS["b"] = b


def init_instrcutions():
    INSTRUCTIONS.setdefault("hlf", hlf)
    INSTRUCTIONS.setdefault("tpl", tpl)
    INSTRUCTIONS.setdefault("inc", inc)
    INSTRUCTIONS.setdefault("jmp", jmp)
    INSTRUCTIONS.setdefault("jie", jie)
    INSTRUCTIONS.setdefault("jio", jio)


def hlf(r):
    REGISTERS[r] = REGISTERS[r] // 2
    return 1 # to increment PC


def tpl(r):
    REGISTERS[r] = REGISTERS[r] * 3
    return 1 # to increment PC


def inc(r):
    REGISTERS[r] = REGISTERS[r] + 1
    return 1 # to increment PC


def jmp(offset):
    return offset # to increment PC


def jie(r, offset):
    if REGISTERS[r] % 2 == 0:
        return offset
    else:
        return 1


def jio(r, offset):
    if REGISTERS[r] == 1:
        return offset
    else:
        return 1


def load(lines):
    program = []
    for line in lines:
        cmd, a, b = parse_line(line)
        if b == None:
            if a.startswith('-') or a.startswith('+'):
                a = int(a)
            program.append((cmd, a))
        else:
            b = int(b)
            program.append((cmd, a, b))
    return program


def parse_line(line):
    pattern = r"(\w+)\s([+-]\d+|\w+),*\s*([+-]\d+)?"
    m = re.search(pattern, line)
    return m.groups()


def run(program):
    pc = 0
    while pc < len(program):
        instruction = program[pc]
        pc += execute(instruction)


def execute(inst):
    if len(inst) == 2:
        return INSTRUCTIONS[inst[0]](inst[1])
    elif len(inst) == 3:
        return INSTRUCTIONS[inst[0]](inst[1], inst[2])


def test():
    with open("testdata") as f:
        lines = f.readlines()
    program = load(lines)
    init()
    run(program)
    print(REGISTERS)


if __name__ == "__main__":
    #test()
    first()
    second()
