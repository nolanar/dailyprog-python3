#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[2015-09-23] Challenge #233 [Intermediate] Game of Text Life

r/dailyprogrammer - https://redd.it/3m2vvk

*TODO*
 - module for producing an animation
"""

import sys
import random

def main():
    with open(sys.argv[1]) as f:
        matrix = [list(line) for line in f.read().splitlines()]
    #Pad rows to uniform length.
    width = max(len(row) for row in matrix)
    matrix = [row + [' '] * (width - len(row)) for row in matrix]
    game = State(matrix)
    game.iterate()
    print('\n', game, sep='')

class State:
    """Object representing the current state of the game.
    """
    def __init__(self, matrix=[[]]):
        self.array = matrix
        
    def iterate(self):
        """Iterate game to next state.
        """
        next_array = []
        for i, row in enumerate(self.array):
            next_array.append([])
            for j, char, in enumerate(row):
                nei = self.neighbours(i, j)
                next_array[i] += (random.choice(nei) if (char == ' ' and len(nei) == 3) else
                                  char if len(nei) in (2,3) else ' ')
        self.array = next_array
            
    def neighbours(self, row, col):
        """Returns a list of neighbouring alive cells.
        """
        width, height = range(len(self.array[row])), range(len(self.array))
        nei_index = ((row + i, col + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0))
        nei_chars = (self.array[i][j] for i, j in nei_index if i in height and j in width)
        return [i for i in nei_chars if i != ' ']

    def __str__(self):
        """2D character array to string.
        """
        return('\n'.join(''.join(row) for row in self.array))
    
if __name__ == '__main__':
    main()