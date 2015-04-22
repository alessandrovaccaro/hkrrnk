#!/usr/bin/env python

import collections, sys


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()))
    
    c = collections.Counter(a)
    count = [c[k] for k in sorted(c)]
    
    for i in range(len(count)):
    	print(sum(count[i:]))


'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
stick=map(int,raw_input().split())
stick=sorted(stick)
print n
for i in xrange(1,n):
    if stick[i]==stick[i-1]: continue
    print n-i
'''

