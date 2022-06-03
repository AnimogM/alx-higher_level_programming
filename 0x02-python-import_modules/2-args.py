#!/usr/bin/env python3

import sys
if __name__ == '__main__':

    n = len(sys.argv)
    if n > 1:
        print(f"{n-1} argument:")
        for i in range(1, n):
            print(f"{i}: {sys.argv[i]}")
    else:
        print("0 arguments.")
