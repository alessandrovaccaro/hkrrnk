#!/opt/local/bin/python3.4
# https://www.hackerrank.com/challenges/insertionsort2

def insert_sort(array):
    ar = array
    for i in range(1, len(ar)):
        val = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > val:
            ar[j + 1] = ar[j]
            j = j - 1
        ar[j + 1] = val
        print(''.join(map(lambda x: '%s ' % x, ar)).strip())
    return ar

if __name__ == "__main__":
    s = int(input())
    ar = [int(x) for x in input().split(' ')]
    insert_sort(ar)

