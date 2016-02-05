#!/usr/bin/env python3

import re

def count_repr(line):
	#print("    Repr: {}, len: {}".format(line, len(line)))
	return len(line)

def count_mem(line):
	pattern = r'\\x[a-f0-9]{2}|(\\")|(\\\\)'
	memline = line.strip('"')
	memline = re.sub(pattern, ".", memline)
	#print("    Mem:  {}, len: {}".format(memline, len(memline)))
	return len(memline)


def count_diff(line):
	return count_repr(line) - count_mem(line)


def first(lines):
	tot_diff = 0
	for line in lines:
		line = line.strip()
		tot_diff += count_diff(line)
		#print()
	print("1. total difference in file: {}".format(tot_diff))


def second(lines):
	tot_diff = 0
	for line in lines:
		line = line.strip()
		enc_line = encode(line)
		tot_diff += count_repr(enc_line) - count_repr(line)
	print("2. total difference in file: {}".format(tot_diff))


def encode(line):
	enc_line = line.replace("\\", "\\\\").replace("\"", "\\\"")
	enc_line = "{}{}{}".format('"', enc_line, '"')
	#print("encode: {} -> {}".format(line, enc_line))
	return enc_line

if __name__ == "__main__":
	f = open("input")
	#f = open("testdata")
	lines = f.readlines()
	f.close()
	first(lines)
	second(lines)
