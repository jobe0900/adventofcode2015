#!/usr/bin/env python3

import re

def has_three_vowels(string):
    vowels = "aeiou"
    count = 0
    for c in vowels:
        count += string.count(c)
        if count >= 3:
            return True
    return False


def has_double_letter(string):
    pattern = r"((\w)\2)"
    return bool(re.search(pattern, string))


def has_forbidden_combination(string):
    forbidden = ["ab", "cd", "pq", "xy"]

    for combo in forbidden:
        if combo in string:
            return True
    return False


def is_nice_string_1(string):
    return has_three_vowels(string) and has_double_letter(string) and not has_forbidden_combination(string)


def has_letter_pair(string):
    pattern = r"(\w{2})+.*\1"
    return bool(re.search(pattern, string))


def has_repeated_letter_with_other_in_middle(string):
    pattern = r"(.)+.{1}\1"
    return bool(re.search(pattern, string))

def is_nice_string_2(string):
    return has_letter_pair(string) and has_repeated_letter_with_other_in_middle(string)


def test():
    s1 = "aei"
    s2 = "xazegov"
    s3 = "aeiouaeiouaeiou"
    print("{} has 3 vowels or more: {}".format(s1, has_three_vowels(s1)))
    print("{} has 3 vowels or more: {}".format(s2, has_three_vowels(s2)))
    print("{} has 3 vowels or more: {}".format(s3, has_three_vowels(s3)))

    s4 = "xx"
    s5 = "abcdde"
    s6 = "aabbccdd"
    print("{} has double letters: {}".format(s4, has_double_letter(s4)))
    print("{} has double letters: {}".format(s5, has_double_letter(s5)))
    print("{} has double letters: {}".format(s6, has_double_letter(s6)))
    print("{} has double letters: {}".format(s3, has_double_letter(s3)))
    print("{} has double letters: {}".format(s1, has_double_letter(s1)))

    print("{} has forbidden combo: {}".format(s4, has_forbidden_combination(s4)))
    print("{} has forbidden combo: {}".format(s6, has_forbidden_combination(s6)))


    s7 = "ugknnbfddgicrmopn"
    s8 = "aaa"
    s9 = "jchzalrnumimnmhp"
    s10 = "haegwjzuvuyypxyu"
    s11 = "dvszwmarrgswjxmb"

    print("{} is nice: {}".format(s7, is_nice_string_1(s7)))
    print("{} is nice: {}".format(s8, is_nice_string_1(s8)))
    print("{} is nice: {}".format(s9, is_nice_string_1(s9)))
    print("{} is nice: {}".format(s10, is_nice_string_1(s10)))
    print("{} is nice: {}".format(s11, is_nice_string_1(s11)))

    s12 = "xyxy"
    s13 = "aabcdefgaa"
    s14 = "aaa"
    print("{} has pairs: {}".format(s12, has_letter_pair(s12)))
    print("{} has pairs: {}".format(s13, has_letter_pair(s13)))
    print("{} has pairs: {}".format(s14, has_letter_pair(s14)))

    s15 = "xyx"
    s16 = "abcdefeghi"
    s17 = "aaa"
    s18 = "aab"
    print("{} has repeat: {}".format(s15, has_repeated_letter_with_other_in_middle(s15)))
    print("{} has repeat: {}".format(s16, has_repeated_letter_with_other_in_middle(s16)))
    print("{} has repeat: {}".format(s17, has_repeated_letter_with_other_in_middle(s17)))
    print("{} has repeat: {}".format(s18, has_repeated_letter_with_other_in_middle(s18)))

    s20 = "qjhvhtzxzqqjkmpb"
    s21 = "xxyxx"
    s22 = "uurcxstgmygtbstg"
    s23 = "ieodomkazucvgmuy"
    print("{} is nice: {}".format(s20, is_nice_string_2(s20)))
    print("{} is nice: {}".format(s21, is_nice_string_2(s21)))
    print("{} is nice: {}".format(s22, is_nice_string_2(s22)))
    print("{} is nice: {}".format(s23, is_nice_string_2(s23)))


def first(f):
    nice_string_count = 0
    for line in f:
        if is_nice_string_1(line):
            nice_string_count += 1
    print("1. Nice strings #: {}".format(nice_string_count))

def second(f):
    nice_string_count = 0
    for line in f:
        if is_nice_string_2(line):
            nice_string_count += 1
    print("2. Nice strings #: {}".format(nice_string_count))


if __name__ == "__main__":
    #test()
    with open("input") as f:
        first(f)
    with open("input") as f:
        second(f)
