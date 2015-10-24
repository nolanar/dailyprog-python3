#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2015-10-14] Challenge #236 [Intermediate] Fibonacci-ish Sequence

r/dailyprogrammer - https://redd.it/3opin7
"""

import sys

def main():
    target = int(sys.argv[1])
    for x in fib_gen(include_seed=False, bound=target):
        if target % x == 0:
            seed = target // x
    for x in fib_gen(seed_value=seed, bound=target):
        print(x)

def fib_gen(include_seed=True, seed_value=1, bound=None):
    """Fibonacci-like sequence generator
    """
    a, b = 0, seed_value
    if include_seed:
        yield a
        yield b
    while True if bound == None else a + b <= bound:
        a, b = b, a + b
        yield b

if __name__ == "__main__":
    main()
