#!/usr/bin/env python3
import re

def first(old_pass):
    new_pass = increment_pass(old_pass)
    while not valid_password(new_pass):
        new_pass = increment_pass(new_pass)
        #print("testing: {} -> {}".format(old_pass, new_pass))
    return new_pass

def valid_password(password):
    return (len(password) == 8) and \
            (password.islower()) and \
            (not contains_i_o_l(password)) and \
            (contains_two_pairs(password)) and \
            (has_three_consecutive_letters(password))

def has_three_consecutive_letters(password):
    for i in range(len(password)-2):
        if (ord(password[i]) == ord(password[i+1]) - 1) and \
                (ord(password[i]) == ord(password[i+2]) - 2):
                    return True
    return False

def contains_two_pairs(password):
    pattern = r"(\w)\1.*(\w)\2"
    m = re.search(pattern , password)
    #if m:
        #print(m.groups())
    return m != None

def contains_i_o_l(password):
    return ('i' in password) or ('o' in password) or ('l' in password)

def increment_pass(password):
    new_pass = list(password)
    inc_pos = -1 #rightmost
    while inc_pos < 0:
        #print("increment: {}".format(new_pass))
        new_pass[inc_pos] = increment_a2z(new_pass[inc_pos])
        inc_pos = calculate_new_inc_pos(new_pass, inc_pos)
    return "".join(new_pass)

def calculate_new_inc_pos(password, inc_pos):
    if password[inc_pos] == 'a': # has wrapped
        inc_pos -= 1
    else:
        inc_pos = 0
    if inc_pos == -1 * len(password): #wrap from beginning again
        inc_pos = -1
    return inc_pos


def increment_a2z(char):
    """increment a-z"""
    if char == 'z':
        c = 'a'
    else:
        c = chr(ord(char)+1)
    return c

def test():
    #p1 = "hijklmmn"
    p1 = "hijklmmz"
    p2 = "aabcdeff"
    p3 = "abbcdeff"
    p4 = "abbceffg"

    #print("{} -> {}".format(p1, increment_pass(p1)))
    #print("{} has 2 pairs: {}".format(p1, contains_two_pairs(p1)))
    #print("{} has 2 pairs: {}".format(p2, contains_two_pairs(p2)))
    #print("{} has 2 pairs: {}".format(p3, contains_two_pairs(p3)))
    #print("{} has 3 consecutive letters: {}".format(p1, has_three_consecutive_letters(p1)))
    #print("{} has 3 consecutive letters: {}".format(p4, has_three_consecutive_letters(p4)))
    #print(increment_a2z('b'))
    #print(increment_a2z('z'))

    test1  = "abcdefgh"
    print("\n{} -> {}".format(test1, first(test1)))
    test2  = "ghijklmn"
    print("\n{} -> {}".format(test2, first(test2)))



if __name__ == "__main__":
    #test()
    passw1 = "hepxcrrq"
    ans1 = first(passw1)
    print("1. FOUND: {} -> {}".format(passw1, ans1))
    ans2 = first(ans1)
    print("2. FOUND: {} -> {}".format(ans1, ans2))
