#!/usr/bin/py
# Head ends here

if __name__ == '__main__':
    N = int(input())
    K = int(input())
    list_n = []
    i = sub_array = 0
    unfairness = 9999999999

    while i < N:
        list_n.append(int(input()))
        i += 1
    i = 0

    list_n.sort()

    while i < N-K:
        sub_array = K + i - 1
        if ( sub_array > (N - 1)):
            break
        new_unfairness = list_n[sub_array] - list_n[i]
        if (new_unfairness < unfairness):
            unfairness = new_unfairness
        i += 1

    print(unfairness)
