#!/usr/bin/env python3

def first():
    with open("input") as f:
        lines = f.readlines()
    replacements = parse_replacements(lines[:-1])
    molecule = lines[-1].strip()
    transforms = transform(molecule, replacements)
    print("1. Nr transformations: {}".format(len(transforms)))


def second():
    with open("input") as f:
        lines = f.readlines()
    replacements = parse_reverse_replacements(lines[:-2])
    sort_replacements(replacements)
    target = lines[-1].strip()
    start = 'e'
    path = reverse_replacement(target, start, replacements)
    print("2. Nr transformations: {}".format(len(path)-1))


def test():
    with open("testdata") as f:
        lines = f.readlines()
    replacements = parse_replacements(lines[:-1])
    molecule = lines[-1].strip()
    #molecule = "HOH"

    print_replacements(replacements)
    print("Molecule: {}".format(molecule))

    transforms = transform(molecule, replacements)
    print(transforms)
    print("Nr transformations: {}".format(len(transforms)))


def test2():
    with open("testdata2") as f:
        lines = f.readlines()
    replacements = parse_reverse_replacements(lines[:-2])
    sort_replacements(replacements)
    print_replacements2(replacements)
    target = lines[-1].strip()
    #target = "HOH"
    print("Molecule: {}".format(target))
    start = 'e'
    path = reverse_replacement(target, start, replacements)
    print("Nr transformations {}".format(len(path)-1))
    for i in path:
        print("\t{}".format(i))


def reverse_replacement(target, start, replacements):
    path = [target]
    last = path[-1]
    while last != start:
        for repl, orig in replacements:
            if repl in last:
                last = last.replace(repl, orig, 1)
                path.append(last)
    return path


# It was too slow to search through all transformations
def breadth_first(start, target, replacements):
    queue = []
    queue.append([start])
    searches = 0
    while queue:
        searches += 1
        if searches % 1000 == 0:
            print(searches)
        path = queue.pop(0)
        last_in_path = path[-1]
        if last_in_path == target:
            return path
        # generate new transformations and add to quemoleculeue
        transforms = transform(last_in_path, replacements)
        #print("{} -> {}".format(last_in_path, transforms))
        for t in transforms:
            new_path = list(path)
            new_path.append(t)
            queue.append(new_path)


def transform(molecule, replacements):
    transforms = set()
    for key in replacements.keys():
        split_molecule = molecule.split(key)
        for i in range(1, len(split_molecule)):
            for v in replacements[key]:
                s = key.join(split_molecule[:i]) + v + key.join(split_molecule[i:])
                #print("TRANS molecule {}: key {}, value {}, i {} => {}".format(molecule, key, v, i, s))
                transforms.add(s)
    return transforms


def parse_replacements(lines):
    replacements = dict()  # key -> [value ...]
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        words = line.split()
        k = words[0]
        v = words[-1]
        replacements.setdefault(k, list()).append(v)
    return replacements


def parse_reverse_replacements(lines):
    replacements = list() # [repl, origin]
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        words = line.split()
        replacement = words[-1]
        origin = words[0]
        replacements.append((replacement, origin))
    return replacements


def sort_replacements(replacements):
    replacements.sort(key=lambda x: len(x[0]), reverse=True)


def print_replacements(replacements):
    print("Replacements")
    for k in replacements.keys():
        print("  {} => {}".format(k, replacements[k]))


def print_replacements2(replacements):
    print("Replacements")
    for r in replacements:
        print("  {} => {}".format(r[0], r[1]))


if __name__ == "__main__":
    #test()
    #test2()
    first()
    second()
