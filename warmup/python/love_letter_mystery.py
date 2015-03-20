#!/usr/bin/py
# Head ends here

if __name__ == "__main__":
    N = int(input())
    result = []
    for i in range(N):
        cur = input()
        length = len(cur)
        moves = k = 0
        while k < length/2:
            moves += abs(ord(cur[k]) - ord(cur[(length - 1) - k]))
            k += 1 
#        print("i {}, moves {}".format(i, moves))
        result.append(moves)
#    print(result)
    for i in result:
        print(i)
