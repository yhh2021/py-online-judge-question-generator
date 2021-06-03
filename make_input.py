#!/usr/bin/env python3

import argparse
import random

def get_random_int(n: int) -> str:
    return ' '.join([ str(random.randrange(10000))
        for _ in range(n) ])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate .in.')
    parser.add_argument('n', type=int,
                        help='how many integers for the input')
    args = parser.parse_args()

    print(get_random_int(args.n))
