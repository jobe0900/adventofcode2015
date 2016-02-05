#!/usr/bin/env python3

def test():
    with open("testdata") as f:
        lines = f.readlines()
    reindeers = parse_lines(lines)
    time = 1000
    winner, longest = get_longest_distance(reindeers, time)
    print(" test1. winner {} flew {} km in time {} s".format(winner, longest, time))

    add_accouting_fields(reindeers)
    collect_points(reindeers, time)
    winner2 = get_most_points(reindeers)
    winner2 = reindeers[winner2]
    print("2. winner {} got {} points for {} km in time {} s".format(winner2["name"], winner2["points"], winner2["distance"], time))



def first(lines):
    reindeers = parse_lines(lines)
    time = 2503
    winner, longest = get_longest_distance(reindeers, time)
    print("1. winner {} flew {} km in time {} s".format(winner, longest, time))


def second(lines):
    reindeers = parse_lines(lines)
    add_accouting_fields(reindeers)
    time = 2503
    collect_points(reindeers, time)
    winnername  = get_most_points(reindeers)
    winner = reindeers[winnername]
    print("2. winner {} got {} points for {} km in time {} s".format(winner["name"], winner["points"], winner["distance"], time))


def add_accouting_fields(reindeers):
    for r in reindeers:
        reindeers[r].setdefault("flight", 0)    # count seconds for this turn
        reindeers[r].setdefault("rest", 0)      # count seconds for this turn
        reindeers[r].setdefault("distance", 0)
        reindeers[r].setdefault("points", 0)    # count collected points


def get_most_points(reindeers):
    leader = None
    most = 0
    for r in reindeers:
        #print("{}: {} km, {} p".format(reindeers[r]["name"],reindeers[r]["distance"],reindeers[r]["points"]))
        if reindeers[r]["points"] > most:
            most = reindeers[r]["points"]
            leader = r
    return leader


def collect_points(reindeers, time):
    longest = 0
    leader = None
    for s in range(time):
        leaders = []
        for r in reindeers:
            tick(reindeers[r])
        award_leaders(reindeers)


def award_leaders(reindeers):
    longest = find_longest_distance(reindeers)
    for r in reindeers:
        if reindeers[r]["distance"] == longest:
            reindeers[r]["points"] += 1


def find_longest_distance(reindeers):
    longest = 0
    for r in reindeers:
        if reindeers[r]["distance"] > longest:
            longest = reindeers[r]["distance"]
    return longest

def tick(reindeer):
    flying = (reindeer["flight"] < reindeer["flytime"])
    if flying:
        reindeer["flight"] += 1
        reindeer["distance"] += reindeer["speed"]
    else:
        reindeer["rest"] += 1
    toggle_fly_rest(reindeer)


def toggle_fly_rest(reindeer):
    if reindeer["rest"] == reindeer["resttime"]:
        reindeer["flight"] = 0
        reindeer["rest"] = 0


def parse_lines(lines):
    reindeers = dict()
    for line in lines:
        reindeer, speed, flytime, resttime = parse_line(line.strip())
        reindeers.setdefault(reindeer, dict()).update(
                {"speed":speed, "flytime":flytime, "resttime":resttime, "name":reindeer})
    return reindeers


def get_longest_distance(reindeers, time):
    longest = 0
    winner = None
    for r in reindeers:
        d = get_distance(reindeers[r], time)
        if d > longest:
            longest = d
            winner = r
    return winner, longest


def get_distance(reindeer, time):
    t = 0
    d = 0
    flying = True
    while t < time:
        dt, dd = run_time(reindeer, t, time, flying)
        flying = not flying
        t += dt
        d += dd
    return d


def run_time(reindeer, t, time, flying = True):
    if flying:
        dt = reindeer["flytime"]
    else:
        dt = reindeer["resttime"]
    if dt > (time - t):
        dt = (time - t)

    if flying:
        dd = fly(reindeer, dt)
    else:
        dd = 0
    return dt, dd


def fly(reindeer, time):
    return reindeer["speed"] * time


def parse_line(line):
    words = line.split()
    reindeer = words[0]
    speed = int(words[3])
    flytime = int(words[6])
    resttime = int(words[-2])
    return reindeer, speed, flytime, resttime

if __name__ == "__main__":
    #test()
    with open("input") as f:
        lines = f.readlines()
        first(lines)
        second(lines)
