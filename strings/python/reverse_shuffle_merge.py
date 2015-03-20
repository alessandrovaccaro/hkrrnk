#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/reverse-shuffle-merge

if __name__ == "__main__":
    s = input()
    half_len = int(len(s)/2)
    substr = []
    letters = {}
    for i in list(s):
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    
    for key, item in letters.items():
         substr.extend([key for x in range(int(item/2))])
    substr.sort()
    res = ''.join(map(lambda x: '%s' % x,substr))

    print(res)
    print(substr.count('o'))
    print(substr.count('u'))
