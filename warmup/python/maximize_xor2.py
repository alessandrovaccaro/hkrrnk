#!/usr/bin/python3
def max_xor(l, r):
    maxxor = 0 
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            max(maxxor, i^j)
    return maxxor

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(max_xor(l, r))
