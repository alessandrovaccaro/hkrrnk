#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/pangrams

if __name__ == "__main__":
    S = input().strip().lower()
    flag = True
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in S:
            flag = False
            break
    if flag:
        print('pangram')
    else:
        print('not pangram')
        
