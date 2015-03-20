#!/usr/bin/python3
def max_xor(l, r):
    maxxor = []
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            print('{} {}'.format(i, j))
            maxxor.append(i ^ j)
    return max(maxxor)

if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print(max_xor(l, r))
