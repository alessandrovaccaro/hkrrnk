#!/usr/bin/env python

if __name__ == "__main__":
    kek = input()
    letters = {}
    count_odd = 0 
    for i in range(len(kek)):
        if kek[i] not in letters:
            letters[kek[i]] = 1
        else:
            letters[kek[i]] += 1
    for key, value in letters.items():
        if value % 2 == 1:
            count_odd += 1

    if (len(kek) % 2 == 0 and count_odd == 0) or (len(kek) % 2 != 0 and count_odd == 1):
        print("YES")
    else:
        print("NO")

#    if len(kek) % 2 == 0:
#        if count_odd == 0:
#            print("YES")
#        else:
#            print("NO")
#    else:
#        if count_odd == 1:
#            print("YES")
#        else:
#            print("NO")

