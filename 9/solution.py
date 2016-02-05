#!/usr/bin/env python3

from itertools import permutations


def first(lines):
	cities, distances = parse_lines(lines)

	perms = permutations(list(cities))
	shortest = ([], float('inf'))
	longest = ([], 0)
	for perm in perms:
		dist = evaluate_path(perm, distances)
		if dist < shortest[1]:
			shortest = perm, dist
		if dist > longest[1]:
			longest = perm, dist
	
	print("Shortest distance: {} for path {}".format(shortest[1], shortest[0]))
	print("Longest distance:  {} for path {}".format(longest[1], longest[0]))


def parse_lines(lines):
	c = set()
	d = dict()

	for line in  lines:
		(source, _, target, _, distance) = line.strip().split()
		c.add(source)
		c.add(target)
		d.setdefault(source, dict())
		d.setdefault(target, dict())
		d[source][target] = int(distance)
		d[target][source] = int(distance)
	
	return c, d


def evaluate_path(path, distances):
	dist = 0
	for i in range(len(path)-1):
		dist += distances[path[i]][path[i+1]]
	return dist


if __name__ == "__main__":
	f = open("input")
	#f = open("testdata")
	lines = f.readlines()
	f.close()

	first(lines)
