from functools import reduce

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        T -= 1
        N, K = [int(x) for x in input().split(' ')]
        arrival = len([x for x in input().split(' ') if int(x) <= 0])
        if arrival >= K:
            print('NO')
        else:
            print('YES')
