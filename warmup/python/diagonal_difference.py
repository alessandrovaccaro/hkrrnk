#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/diagonal-difference

'''
Sample Input

3
11 2 4
4 5 6
10 8 -12

Sample Output

15

'''

if __name__ == "__main__":
    matrix_s = int(input().strip())
    matrix = []
    while(matrix_s > 0):
        matrix.append(list(map(int, input().strip().split(' '))))
        matrix_s -= 1

    left_right, right_left = 0,0

    for i in range(0, len(matrix)):
        left_right += matrix[i][i]

    for i in range(len(matrix)-1, -1, -1):
        right_left += matrix[i][(len(matrix)-1)-i]
#        print('%d - %d' % (i, (len(matrix)-1)-i))

#    print('left_right %s, right_left %s' % (left_right, right_left))
    print(abs(right_left - left_right))

