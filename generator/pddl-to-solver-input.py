#! /usr/bin/env python3

import os
import subprocess
import sys
import re

color_to_position = {
    'white': 'F',  # front
    'blue': 'L',  # left
    'red': 'U',  # up
    'orange': 'D',  # down
    'green': 'R',  # right
    'yellow': 'B',  # back
}

SOLVED_CUBE = [
    "UF", "UR", "UB", "UL",
    "DF", "DR", "DB", "DL",
    "FR", "FL", "BR", "BL",
    "UFR", "URB", "UBL", "ULF",
    "DRF", "DFL", "DLB", "DBR",
]

def find_matching_cubie(cubie, goal):
    for cubie_id in goal:
        colors = goal[cubie_id]
        if len(cubie) != len(colors):
            continue  # comparing corner to edge

        match = True
        for color in colors:
            pos = color_to_position[color]
            if not pos in cubie:
                match = False
                break
        if match:
            return cubie_id

    assert(False)

def construct_init_pos(cubie, init, goal):
    assert(len(cubie) == len(init))
    assert(len(init) == len(goal))

    init_pos = ""
    for pos in cubie:
        for i in range(len(goal)):
            translated_color = color_to_position[goal[i]]
            if translated_color == pos:
                init_pos += color_to_position[init[i]]
                break

    assert(len(init_pos) == len(cubie))
    return init_pos

def generate_sequence(init, goal):
    seq = []
    for cubie in SOLVED_CUBE:
        cubie_id = find_matching_cubie(cubie, goal)
        init_colors = init[cubie_id]
        goal_colors = goal[cubie_id]
        init_pos = construct_init_pos(cubie, init_colors, goal_colors)
        seq.append(init_pos)

    return seq

def toCubies(s):
    s = s.strip(' \t\n()')
    s = re.split(r'\)\s*\(', s)
    s = [x.strip().split() for x in s]

    cubies = {}
    for atom in s:
        if atom[0].startswith('cube'):
            cid = atom[0][4:]
            cubies[cid] = atom[1:]

        elif atom[0].startswith('edge'):
            eid = atom[0][4:]
            cubies[eid] = atom[1:]
    return cubies

def main(filename):
    content = open(filename, 'r').read()
    content = re.sub(r';.*\n', '', content)
    content = re.sub(r'\s+', ' ', content)

    init_pat = r'\(:init\s*((\(cube[0-9][^)]+\)\s*|\(edge[0-9][^)]+\)\s*)+)\s*\)'
    goal_pat = r'\(:goal\s*\(\s*and\s*((\(cube[0-9][^)]+\)\s*|\(edge[0-9][^)]+\)\s*)+)\s*\)\s*\)'
    #init_match = re.search(r'\(:init\s*(\(cube[0-9][^)]+\)\s*|\(edge[0-9][^)]+\)\s*)\s*\)', content)
    init_match = re.search(init_pat, content)
    assert(init_match is not None)
    init = toCubies(init_match.group(1))

    goal_match = re.search(goal_pat, content)
    assert(goal_match is not None)
    goal = toCubies(goal_match.group(1))

    seq = generate_sequence(init, goal)
    print(' '.join(seq))
    #process = subprocess.run('./optimal-solver', input=seq, text=True)

if __name__ == '__main__':
    main(sys.argv[1])
