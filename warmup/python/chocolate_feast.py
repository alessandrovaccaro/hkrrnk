from math import floor
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        answer = 0
        N,C,M = [int(x) for x in input().split(' ')]
        # Compute Answer
        print('%d' % (floor(N/C) + (floor(N/C) - 1) / (M - 1)))

