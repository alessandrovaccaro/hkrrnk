#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    answer = 0
    occ = {}
    #count occurrencies
    for i in range(len(b)):
        if b[i] not in occ:
            occ[b[i]] = 1
        else:
            occ[b[i]] = occ[b[i]] + 1
    #find lonely integer
    for key, value in occ.items():
        if value == 1:
            answer = key
    return answer
# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = list(map(int, input().strip().split(" ")))
    print(lonelyinteger(b))
