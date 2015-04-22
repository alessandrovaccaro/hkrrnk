#!/opt/local/bin/python3.4
# Kadane algorithm
# https://www.hackerrank.com/challenges/maxsubarray

def max_sum_subarray(L):
    current_sum = best_sum_cont = best_sum_non_cont = 0
    current_index = best_s_index = best_e_index = -1

    for i in range(len(L)):
        val = current_sum + L[i]
        if val > current_sum:
            if current_sum == 0:
                current_index = i
            current_sum = val
        else:
            current_sum = val 
        if current_sum > best_sum:
            best_sum = current_sum
            best_s_index = current_index
            best_e_index = i
    return {'best_sum_cont':best_sum_cont, 'best_sum_non_cont': best_sum_non_cont}


if __name__ == '__main__':
    print(max_sum_subarray([-1,-3, 11,-2,1,5,-100, 100,99,-120, 300]))
