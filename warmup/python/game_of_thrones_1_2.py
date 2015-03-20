#!/usr/bin/env python

if __name__ == "__main__":
    kek = list(input())
    count_odd = 0 

    print(kek)
# CAZZATEEEEE

#!!!!!
    for i in kek:
        count_odd += kek.count(i) % 2
    
    print("count {}".format(count_odd))

    if (len(kek) % 2 == 0 and count_odd == 0) or (len(kek) % 2 != 0 and count_odd == 1):
        print("YES")
    else:
        print("NO")
