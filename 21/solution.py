#!/usr/bin/env python3

from collections import namedtuple
import re

Item = namedtuple("Item", "name, cost, damage, armor")

# ---------------------------------------------------------------
class Player():
    def __init__(self, name, hit_points, damage_score, armor_score):
        self.name = name
        self.hit_points = hit_points
        self.damage_score = damage_score
        self.armor_score = armor_score
        self.spent = 0
        self.items = {
                "Weapon": None,
                "Armor": None,
                "Rings": []}

    def damage(self):
        return self.damage_score

    def armor(self):
        return self.armor_score

    def health(self):
        return self.hit_points

    def take_hit(self, hit_value):
        self.hit_points -= hit_value

    def add_item(self, category, item):
        if category in ("Weapon", "Armor"):
            if self.items[category] != None:
                print("Cannot add another: ", category)
            else:
                self.items[category] = item
                self.spent += item.cost
                self.damage_score += item.damage
                self.armor_score += item.armor
        elif category == "Rings":
            if len(self.items["Rings"]) >= 3:
                print("Too many rings. Cannot add:", item)
            else:
                self.items[category].append(item)
                self.spent += item.cost
                self.damage_score += item.damage
                self.armor_score += item.armor
        self.items[category]

# ---------------------------------------------------------------

def first():
    shop = read_shop_file()

    buy_orders = generate_buy_orders(shop)
    least_cost = float("Inf")
    winner_items = None
    for order in buy_orders:
        player = Player("Player", 100, 0, 0)
        boss = Player("Boss", 104, 8, 1) # from input file
        players = [player, boss]
        buy(shop, player, order)
        winner = play_game(players)
        if winner == player and player.spent < least_cost:
            least_cost = player.spent
            winner_items = player.items.copy()
    print("1. Least cost for winning:", least_cost)
    print("    items:")
    for item in winner_items:
        print("        ", winner_items[item])


def second():
    shop = read_shop_file()

    buy_orders = generate_buy_orders(shop)
    highest_cost = 0
    winner_items = None
    for order in buy_orders:
        player = Player("Player", 100, 0, 0)
        boss = Player("Boss", 104, 8, 1) # from input file
        players = [player, boss]
        buy(shop, player, order)
        winner = play_game(players)
        if winner != player and player.spent > highest_cost:
            highest_cost = player.spent
            winner_items = player.items.copy()
    print("2. Highest cost for losing:", highest_cost)
    print("    items:")
    for item in winner_items:
        print("        ", winner_items[item])


def test():
    player = Player("Player", 8, 5, 5)
    boss = Player("Boss", 12, 7, 2)
    winner = play_game([player, boss])
    print("Winner", winner.name)


def read_shop_file():
    with open("shop") as f:
        lines = f.readlines()
    shop = {"Weapons": [],
            "Armor":   [],
            "Rings":   []}
    category = ""
    category_pattern = r"(\w+):[\s+\w+]{3}"
    item_pattern = r"(\w+ \+?\d*)\s+(\d+)\s+(\d+)\s+(\d+)"
    for line in lines:
        line = line.strip()
        match = re.match(category_pattern, line)
        if match:
            category = match.group(1)
            continue
        match = re.match(item_pattern, line)
        if match:
            name = match.group(1).strip()
            cost = int(match.group(2))
            damage = int(match.group(3))
            armor = int(match.group(4))
            item = Item(name, cost, damage, armor)
            shop[category].append(item)
    return shop


def generate_buy_orders(shop):
    """Generate list of items to by for categories:
        weapon, armor, ring1, ring2, ring3
        0 = no buy, 1.. = buy item nr in list"""
    orders = []
    for weapon_nr in range(1, len(shop["Weapons"]) + 1): # start at 1 = mandatory
        for armor_nr in range(len(shop["Armor"]) + 1):
            for ring1_nr in range(len(shop["Rings"]) + 1):
                for ring2_nr in range(len(shop["Rings"]) + 1):
                    if ring1_nr != 0 and ring2_nr == ring1_nr:
                        continue
                    for ring3_nr in range(len(shop["Rings"]) + 1):
                        if (ring1_nr != 0 and ring3_nr == ring1_nr) or \
                                (ring2_nr != 0 and ring3_nr == ring2_nr):
                                    continue
                        orders.append([weapon_nr, armor_nr, ring1_nr, ring2_nr, ring3_nr])
    return orders


def buy(shop, player, order):
    player.add_item("Weapon", shop["Weapons"][order[0]-1])
    if order[1] > 0:
        player.add_item("Armor", shop["Armor"][order[1]-1])
    if order[2] > 0:
        player.add_item("Rings", shop["Rings"][order[2]-1])
    if order[3] > 0:
        player.add_item("Rings", shop["Rings"][order[3]-1])
    if order[4] > 0:
        player.add_item("Rings", shop["Rings"][order[4]-1])


def play_game(players):
    turn = 0
    winnner = None
    while True:
        attacker = players[turn % 2]
        defender = players[(turn + 1) % 2]
        hit_value = attacker.damage() - defender.armor()
        if hit_value < 0:
            hit_value = 1
        defender.take_hit(hit_value)
        #print("{attacker}, deals {hit} damage, {defender} goes down to {health}".format(
            #attacker=attacker.name, hit=hit_value, defender=defender.name, health=defender.health()
            #))
        if defender.health() <= 0:
            return attacker
        turn = (turn + 1) % 2


if __name__ == "__main__":
    #test()
    first()
    second()
