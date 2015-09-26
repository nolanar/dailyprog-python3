#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[2015-09-21] Challenge #233 [Easy] The house that ASCII built

r/dailyprogrammer - https://redd.it/3ltee2

Changes from description:
 - First line number unnessisary (but allowed).
 - ASCII art style changed somewhat.
"""

import sys
import random
from itertools import zip_longest

# Building characters.
BLUEPRINT = '*'
BEAM = '-'
HI_BEAM = '¯'
WALL = '|'
BOTTOM_CORNER = '\''
TOP_CORNER = '.'
FORW_ROOF = '/'
BACK_ROOF = '\\'
PEAK = '.'
WINDOW = 'o'
BLANK = ' '

def main():
    # Read from blueprint file.
    with open(sys.argv[1], 'r') as f:
        blueprint = f.read()
    
    # 2D-array of 1 (if BLUEPRINT) and 0 (otherwise) from blueprint.
    heights = [[1 if ch == BLUEPRINT else 0 for ch in line] for line in blueprint.split('\n')]
    
    # Add rows to give list of tower heights.
    zipped = zip_longest(*heights, fillvalue=0)
    heights = [sum(tup) for tup in zipped] + [0]

    # Construct sideways building from towers.
    door_pos = random.randrange(len(heights) - 1)
    side_building = []
    prev = 0
    width = 1
    tower_index = 0
    for i in range(len(heights) - 1):
        current, nxt = heights[i], heights[i + 1]
        if current == nxt:
            width += 1
        else:
            side_building += tower(width, current, prev, door=(door_pos - tower_index))
            # Initialise next tower.
            prev = current
            width = 1
            tower_index = i + 1
    # Rightmost wall.
    side_building += tower(0, 0, prev)
   
    # Correct orientation and print:
    out = '\n'.join(rotate(side_building))
    print(out)
    with open('output - ' + sys.argv[1], 'w') as f:
        f.write(out)
            
def tower(width, floors, wall, door=-1):
    """Creates a sideways tower.
    """
    # Create walls.
    left_wall = BEAM + BLANK * (2*min(floors, wall) - 1) if min(floors, wall) else ''
    left_wall += BOTTOM_CORNER + WALL * (2*abs(floors - wall) - 1) + TOP_CORNER
    side_tower = [left_wall]
    blank_seg = BEAM + BLANK * (2*floors - 1) + BEAM
    door_seg = BEAM + WALL + BLANK * 2*(floors - 1) + BEAM
    for col in range(width):
        if col == door:
            side_tower.extend([door_seg, window_seg(floors, is_door=False), door_seg])
        else:
            side_tower.extend([blank_seg, window_seg(floors), blank_seg])
        if col != width - 1:
            side_tower.append(blank_seg)
        
    # Create roof.
    if width:
        peak = 2*width
        side_tower[peak] += BLANK * (peak - 1) + PEAK
        for col in range(peak -  1):
            side_tower[col + 1] += BLANK * col + FORW_ROOF
            side_tower[-(col + 1)] += BLANK * col + BACK_ROOF

    return side_tower

def window_seg(floors, is_door=True):
    """Randomly generated window segment of tower.
    """
    windowed = BEAM + (random.choice([' ', WINDOW]) if is_door else HI_BEAM)
    for _ in range(1, floors):
        windowed += BLANK + random.choice([' ', WINDOW])
    return windowed + BEAM
    
def rotate(string_list):
    """ Rotate list of strings anti-clocwise 90 degrees.
    """
    char_mat = [list(string) for string in string_list]
    tr_char_mat = zip_longest(*char_mat, fillvalue=' ')
    return reversed([''.join(char_list) for char_list in tr_char_mat])
    
if __name__ == "__main__":
    main()
