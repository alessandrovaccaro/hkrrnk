#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N, C, M = list(int(x) for x in sys.stdin.readline().split())
        
        total = N // C
        wrappers = total
        
        while wrappers >= M:
            wrappers += 1 - M
            total += 1
        
        print(total)