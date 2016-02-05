#!/usr/bin/env python3

def first(indata, rounds):
    i = "{}".format(indata)

    outdata = look_and_say(i, rounds)
    print("{} -> length {} after {} rounds".format(indata, len(outdata), rounds))


def second(indata, rounds):
    first(indata, rounds)


def look_and_say(indata, rounds):
    outdata = indata

    for i in range(rounds):
        outdata = transform(outdata)

    return outdata


def transform(indata):
    outdata = ""

    current = ""
    run_count = 1
    i = 0

    while i < len(indata):
        current = indata[i]
        i += 1
        while i < len(indata) and indata[i] == current:
            run_count += 1
            i += 1
        outdata += "{}{}".format(run_count, current)
        run_count = 1

    return outdata


if __name__ == "__main__":
    indata = 1113122113
    rounds_1 = 40
    rounds_2 = 50

    first(indata, rounds_1)
    second(indata, rounds_2)

