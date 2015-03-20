#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    answer = 0
    for i in range(len(b)):
        answer = answer ^ b[i]
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().strip().split(" ")))
    print(lonelyinteger(b))
