from math import sqrt, floor, ceil

'''
Method 1: O(root(B))
We have to find number of square numbers (numbers of the form X*X, X>0) between A and B (1 <= A,B<= 10^9).

We run a loop from i=1 and check if (i*i) lies between A and B (both inclusive). Once i*i > B, all further i will never satisfy the condition, so we break here.

Method 2: O(1)

We can simply take a√ and b√ and count numbers between them using
⌊b√⌋−⌈a√⌉+1
'''

def perfect_square1(a, b):
    i = floor(sqrt(a))
    ans = 0
    while 1:
        k = i * i
        i += 1
        if ( k >= a and k <= b ):
            ans += 1
        elif (k >= b):
            break
    return ans

def perfect_square2(a, b):
    return floor(sqrt(b)) - ceil(sqrt(a)) + 1

if __name__ == "__main__":
    T = int(input())
    while T > 0:
        T -= 1
        A, B = map(int, input().split(' '))
        print(perfect_square1(A, B))

