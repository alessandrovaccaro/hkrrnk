#!/usr/bin/python3
def ababa(l):
    deletion = 0
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            deletion = deletion + 1
    return deletion
        

if __name__ == '__main__':
    
    i = int(input())
    seq = []
    for idx in range(i):
        seq.append(input())
    for item in seq:
        print(ababa(item))
