#!/usr/bin/env python
import hashlib


def create_string_to_hash(key, nr):
    return "{}{}".format(key, nr)

def create_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def matches_5_zeroes(string):
    return string.startswith("00000")

def startswith_zeroes(nr_zeroes, string):
    subs = "0"* nr_zeroes
    return string.startswith(subs)


def first(key):
    nr = 1

    string = create_string_to_hash(key, nr)
    hashstring = create_hash(string)
    
    while not startswith_zeroes(5, hashstring):
        nr += 1
        string = create_string_to_hash(key, nr)
        hashstring = create_hash(string)

    print("1. First hash for key {}: {}".format(key, nr))
    return nr

def second(key):
    nr = 1

    string = create_string_to_hash(key, nr)
    hashstring = create_hash(string)
    
    while not startswith_zeroes(6, hashstring):
        nr += 1
        string = create_string_to_hash(key, nr)
        hashstring = create_hash(string)

    print("2. First hash for key {}: {}".format(key, nr))
    return nr


def test():
    print(create_string_to_hash("abc", 1))

    string = "abcdef609043"
    print(create_hash(string))

    s1 = "abgdef3545"
    s2 = "00000bfd21"
    print("{} matches zeroes: {}".format(s1, startswith_zeroes(5, s1)))
    print("{} matches zeroes: {}".format(s2, startswith_zeroes(5, s2)))

    print(first("abcdef"))

if __name__ == "__main__":
    #test()
    first("ckczppom")
    second("ckczppom")
