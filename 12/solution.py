#!/usr/bin/env python3

import re
import json

def first(indata):
    return sum_string(indata)


def sum_string(string):
    pattern = r"-?\d+"
    total = 0
    matches = re.findall(pattern, string)
    for m in matches:
        total += int(m)
    return total


def second(indata):
    return eval_json(json.loads(indata))


def eval_json(data):
    if type(data) == int:
        return data
    elif type(data) == dict:
        if "red" in data.values():
            return 0
        return sum(map(eval_json, data.values()))
    elif type(data) == list:
        return sum(map(eval_json, data))
    else:
        return 0

def test():
    teststrings1 = [
            "[1,2,3]",
            "{'a':2, 'b':4}",
            "[[[3]]]",
            "{'a':{'b':4}, 'c':-1 }",
            "{'a':[-1,1]}",
            "[-1,{'a':1}]",
            "[]",
            "{}"
            "[46, 16]"
        ]

    print("TEST 1")
    for ts in teststrings1:
        print("sum {} = {}".format(ts, sum_string(ts)))

    teststrings2 = [
            '[1,2,3]',
            '[1,{"c":"red", "b":2}, 3]',
            '{"a":1,"b":["red", 2], "c":3}',
            '{"a":1,"b":["red", {"c":"red"}], "d":3}',
            '{"d":"red", "e":[1,2,3,4],"f":5, "g":{"h":10}}',
            '{"a":13, "d":"red", "e":[1,2,3,4],"f":5, "g":{"h":10}}',
            '[1, "red", 5]'
        ]
    print("\n\nTEST 2")
    for ts in teststrings2:
        print("sum {} = {}".format(ts, second(ts)))


if __name__ == "__main__":
    #test()

    with open("input") as f:
        indata = f.read()

    first(indata.strip())
    print("1. sum: {}".format(first(indata.strip())))
    second(indata.strip())
    print("2. sum: {}".format(second(indata.strip())))
