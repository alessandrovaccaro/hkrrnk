#!/usr/bin/python

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        T -= 1;
        count = 0
        N = int(input())
        a = [int(i) for i in list(str(N)) if i != '0']
        for k in a:
            if N % k == 0:
                count += 1
        print(count)
