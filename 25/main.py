#!/usr/bin/env python3
import sys
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-n', type=int, default=None, help="fib sequence n")
parser.add_argument('-l', '--length', type=int, default=None,
                    help="fib sequence n")


def fib(n):
    if n <= 1:
        return n
    prev1 = 0
    prev2 = 1
    for i in range(2, n):
        prev1, prev2 = prev2, prev1 + prev2
    return prev1 + prev2


def find_length(length):
    i = 0
    while True:
        f = fib(i)
        fib_length = len(str(f))
        # print(f'i = {i}, f = {f}, fib_length = {fib_length}')
        if fib_length >= length:
            break
        i += 1
    return i


def main():
    args = parser.parse_args()
    if args.n is not None:
        print(fib(args.n))
        return
    print(find_length(args.length))


if __name__ == "__main__":
    sys.exit(main())
