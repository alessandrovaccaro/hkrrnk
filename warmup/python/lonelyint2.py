#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    answer = 0
    for i in b:
        if b.count(x) == 1:
            answer = 0
            break
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
