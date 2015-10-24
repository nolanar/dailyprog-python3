#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    target = int(input("Input: "))
    for x in fib_gen(include_seed=False, bound=target):
        if target % x == 0:
            seed = target // x
    for x in fib_gen(seed_value=seed, bound=target):
        print(x)

def fib_gen(include_seed=True, seed_value=1, bound=None):
    a, b = 0, seed_value
    if include_seed:
        yield a
        yield b
    while True if bound == None else a + b <= bound:
        a, b = b, a + b
        yield b

if __name__ == "__main__":
    main()
