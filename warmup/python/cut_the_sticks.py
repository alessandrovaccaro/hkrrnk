#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/cut-the-sticks

def count_cut( stick_list , min_len ):
    res = 0
    for i in stick_list:
        if (i >= min_len): res += 1
    return res
    

if __name__ == '__main__':
    N = int(input())
    sticks = [int(x) for x in input().strip().split(' ')]
    short = min(filter(None,sticks))
 
    while(N >= 1):
#        print("N: %d, short: %d, " % (N, short), end="")
#        print(sticks)
        print(N)
        sticks = [(i - short) if i >= short else i for i in sticks]
        if(sticks.count(0) < len(sticks)):
            short = min(filter(None,sticks))
            N = count_cut(sticks, short)
        else:
            N = 0

