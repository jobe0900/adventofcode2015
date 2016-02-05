#!/usr/bin/env python3

from collections import namedtuple
import itertools

Ingredient = namedtuple("Ingredient", "name, capacity, durability, flavor, texture, calories")

def test():
    with open("testdata") as f:
    #with open("input") as f:
        lines = f.readlines()
    #first(lines)
    second(lines)


def first(lines):
    ingredients = parse_lines(lines)
    best, score = find_best_mix(ingredients)
    print("1. Best score: {} for mix {}".format(score, mix_as_string(best, ingredients)))

def second(lines):
    ingredients = parse_lines(lines)
    best, score = find_best_mix(ingredients, calories=500)
    print("2. Best score: {} for mix {}".format(score, mix_as_string(best, ingredients)))

def parse_lines(lines):
    ingredients = []
    for line in lines:
        ingredient = parse_line(line.strip())
        #print_ingredient(ingredient)
        ingredients.append(ingredient)
    return ingredients


def mix_as_string(mix, ingredients):
    s = []
    for i in range(len(mix)):
        s.append("\n\t{:>3} spoons {}".format(mix[i], ingredients[i].name))
    return ", ".join(s)


def find_best_mix(ingredients, calories=0):
    combs = generate_combinations(len(ingredients))

    best = ()
    highest = 0
    for c in combs:
        score, cals = calculate_combination_score(c, ingredients)
        #if c[0] == 21:
            #print("{} -> {}".format(c, score))
        #print("Calculated combination {} for score {}".format(c, score))
        if (cals == calories or calories == 0) and (score > highest):
            highest = score
            best = c


    return best, highest


def calculate_combination_score(combination, ingredients):
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    cals = 0
    for i in range(len(combination)):
        capacity += combination[i] * ingredients[i].capacity
        durability += combination[i] * ingredients[i].durability
        flavor += combination[i] * ingredients[i].flavor
        texture += combination[i] * ingredients[i].texture
        cals += combination[i] * ingredients[i].calories
    #print("Calc comb: {}, {}, {}, {}".format(capacity, durability, flavor, texture))
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0, 0
    #print("  Calc comb: {}, {}, {}, {}".format(capacity, durability, flavor, texture))
    return capacity * durability * flavor * texture, cals


def generate_combinations(length):
    c = []
    #for i in combinations_with_replacement(range(100), length):
    for i in itertools.product(range(100 + 1), repeat=length):
        if sum(i) == 100:
            c.append(i)
    #for i in range(len(c)):
        ##if i % 10 == 0:
        #if i % 100 == 0:
            #print("    {}. Combination {}".format(i, c[i]))
    return c

def parse_line(line):
    words = line.split()
    name = words[0].strip(':')
    capacity = int(words[2].strip(','))
    durability = int(words[4].strip(','))
    flavor = int(words[6].strip(','))
    texture = int(words[8].strip(','))
    calories = int(words[-1])

    ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
    return ingredient

def print_ingredient(ing):
    print("{}: Capacity {}, Durability {}, Flavor {}, Texture {}, Calories {}".format(
        ing.name, ing.capacity, ing.durability, ing.flavor, ing.texture, ing.calories
        ))

if __name__ == "__main__":
    #test()
    with open("input") as f:
    #with open("testdata") as f:
        lines = f.readlines()
        first(lines)
        second(lines)
