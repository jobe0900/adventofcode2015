#!/usr/bin/env python3

import itertools
import operator


def test():
    with open("testdata") as f:
    #with open("input") as f:
        lines = f.readlines()
    packages = [int(x) for x in lines]
    #print(weights, sum(weights))

    nr_containers = 3   # 0 = passenger, 1 and 2 = side
    container_payload = sum(packages) // nr_containers

    container_distributions = calc_container_distributions(packages, nr_containers)
    container_distributions = make_container_smallest(container_distributions, 0) # cont 0 = passenger compartement
    print("Container Distributions: ", container_distributions)

    cont0_options = find_matching_container_0(packages, container_distributions, container_payload)
    quantum_entanglement = find_quantum_entanglement(cont0_options)
    print("Smallest Quantum Entanglement: ", quantum_entanglement)


def test2():
    with open("testdata") as f:
    #with open("input") as f:
        lines = f.readlines()
    packages = [int(x) for x in lines]
    #print(weights, sum(weights))

    nr_containers = 4   # 0 = passenger, 1 and 2 = side
    container_payload = sum(packages) // nr_containers

    container_distributions = calc_container_distributions(packages, nr_containers)
    container_distributions = make_container_smallest(container_distributions, 0) # cont 0 = passenger compartement
    print("Container Distributions: ", container_distributions)

    cont0_options = find_matching_container_0(packages, container_distributions, container_payload)
    quantum_entanglement = find_quantum_entanglement(cont0_options)
    print("Smallest Quantum Entanglement: ", quantum_entanglement)



def first():
    with open("input") as f:
        lines = f.readlines()
    packages = [int(x) for x in lines]

    nr_containers = 3   # 0 = passenger, 1 and 2 = side
    container_payload = sum(packages) // nr_containers

    container_distributions = calc_container_distributions(packages, nr_containers)
    container_distributions = make_container_smallest(container_distributions, 0) # cont 0 = passenger compartement

    cont0_options = find_matching_container_0(packages, container_distributions, container_payload)
    quantum_entanglement = find_quantum_entanglement(cont0_options)
    print("1. Smallest Quantum Entanglement: ", quantum_entanglement)

def second():
    with open("input") as f:
        lines = f.readlines()
    packages = [int(x) for x in lines]

    nr_containers = 4   # 0 = passenger, 1 and 2 = side, 3 = trunk
    container_payload = sum(packages) // nr_containers

    container_distributions = calc_container_distributions(packages, nr_containers)
    container_distributions = make_container_smallest(container_distributions, 0) # cont 0 = passenger compartement

    cont0_options = find_matching_container_0(packages, container_distributions, container_payload)
    quantum_entanglement = find_quantum_entanglement(cont0_options)
    print("2. Smallest Quantum Entanglement: ", quantum_entanglement)


def calc_container_distributions(packages, nr_containers):
    distribution =  [sorted(x) for x in itertools.permutations((range(len(packages))), nr_containers) 
            if sum(x) == len(packages) and 0 not in x]
    distribution = unique_list(distribution)
    return distribution


def make_container_smallest(distribution, container_nr):
    new_dist = []
    nr_containers = len(distribution[0])
    for comb in distribution:
        valid = True
        for i in range(nr_containers):
            if comb[container_nr] > comb[i]:
                valid = False
        if valid:
            new_dist.append(comb)
    return new_dist


def find_matching_container_0(packages, distributions, weight):
    cont0_packs = find_smallest_containers(packages, weight)
    if cont0_packs == []:
        print("No solution. Cont0 []")
        return None
    return cont0_packs


def find_smallest_containers(packages, weight):
    for length in range(1, len(packages)):
       cont = [sorted(x) for x in itertools.permutations(packages, length) if sum(x) == weight]
       if cont != []:
           return unique_list(cont)
    return []


def find_quantum_entanglement(cont0_options):
    quantum_entanglement = float('Inf')
    for p in cont0_options:
        qe = list(itertools.accumulate(p, operator.mul))[-1]
        quantum_entanglement = min(quantum_entanglement, qe)
    return quantum_entanglement

def unique_list(lst):
    unique = []
    [unique.append(x) for x in lst if x not in unique]
    return unique


if __name__ == "__main__":
    #test()
    #test2()
    first()
    second()
