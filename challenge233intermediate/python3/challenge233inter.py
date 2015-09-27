#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[2015-09-23] Challenge #233 [Intermediate] Game of Text Life

r/dailyprogrammer - https://redd.it/3m2vvk

*TODO*
 - class for game state
 - module for producing an animation
"""

import sys
import random

def main():
    with open(sys.argv[1]) as f:
        state = [list(line) for line in f.read().splitlines()]
    #Pad rows to uniform length.
    width = max(len(row) for row in state)
    state = [row + [' '] * (width - len(row)) for row in state]
    
    next_state = iter_state(state)
    print('\n' + to_string(next_state))
    
def iter_state(state):
    """Iterate game to next state.
    """
    next_state = []
    for i, row in enumerate(state):
        next_state.append([])
        for j, char, in enumerate(row):
            nei = neighbours(state, i, j)
            next_state[i] += (random.choice(nei) if (char == ' ' and len(nei) == 3) else
                              char if len(nei) in (2,3) else ' ')
    return next_state
        
def neighbours(state, row, col):
    """Returns a list of neighbouring alive cells.
    """
    width, height = range(len(state[row])), range(len(state))
    nei_index = ((row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0))
    nei_chars = (state[i][j] for i, j in nei_index if i in height and j in width)
    return [i for i in nei_chars if i != ' ']

def to_string(matrix):
    """2D character array to string.
    """
    return('\n'.join(''.join(row) for row in matrix))
    
if __name__ == '__main__':
    main()