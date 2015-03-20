# https://www.hackerrank.com/challenges/insertionsort1

if __name__ == "__main__":
    s = int(input()) - 1
    ar = [int(x) for x in input().split(' ')]

    for i in range(s, -1, -1):
        val = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > val:
            ar[j + 1] = ar[j]
            print(''.join(map(lambda x: '%s ' % x, ar)).strip())
            j = j - 1
        ar[j + 1] = val

    print(''.join(map(lambda x: '%s ' % x, ar)).strip())
