#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""[2015-09-23] Challenge #233 [Intermediate] Game of Text Life

r/dailyprogrammer - https://redd.it/3m2vvk
"""

import sys
from numpy import array

def main():
    #Read from file.
    with open(sys.argv[1]) as f:
        thing = array([list(_) for _ in f.read().split('\n')])
        
    print(thing)

if __name__ == '__main__':
    main()