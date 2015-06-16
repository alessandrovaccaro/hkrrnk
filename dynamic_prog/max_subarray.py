#!/opt/local/bin/python3.4
# Kadane algorithm
# https://www.hackerrank.com/challenges/maxsubarray

def max_sum_subarray(L):
    current_sum = best_sum = 0
    non_cont = 0

    for i in range(len(L)):
        val = current_sum + L[i]
        val_non = non_cont + L[i]
        if val_non > non_cont:
           non_cont += L[i]

        if val > 0:
            current_sum = val
        else:
            current_sum = 0
        if current_sum > best_sum:
            best_sum = current_sum
    if non_cont == 0: non_cont = max(L)
    if best_sum == 0: best_sum = non_cont
    return (best_sum, non_cont)


if __name__ == '__main__':
    T = int(input().strip())
    while(T):
        N = int(input().strip())
        l = [int(x) for x in input().strip().split(' ')]
        print('%d %d' % max_sum_subarray(l))
        T -= 1
