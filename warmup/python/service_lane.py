#!/usr/bin/python3

if __name__ == "__main__":
    N, T = [int(x) for x in input().strip().split(' ')]
    lane = [int(x) for x in input().strip().split(' ')]
    while(T):
        a, b = [int(x) for x in input().strip().split(' ')]
        print(min(lane[a:b+1]))
        T -= 1
