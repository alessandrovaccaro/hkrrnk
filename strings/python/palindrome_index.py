#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/palindrome-index

def check_palindrome(s):
    index = -1
    lng = len(s)
    for i in range(int(lng/2)):
        if s[i] != s[lng - i - 1]:
            if is_palindrome(s[(i+1):(lng-i)]):
                index = i
            else:
                index = lng - i - 1
            break
    return index

def is_palindrome(s):
    p = 0
    for i in range(int(len(s)/2)):
        if s[i] == s[len(s) - 1 - i]:
            p += 1
    return p == int(len(s)/2)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        palin = input()
        print(check_palindrome(palin))

