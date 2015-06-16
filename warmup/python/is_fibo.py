#!/opt/local/bin/python3.4
#https://www.hackerrank.com/challenges/is-fibo

if __name__ == "__main__":
    fibonacci = [0] * 51
    fibonacci[1] = 1

    for i in range(2,51):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]

    T = int(input().strip())
    while(T > 0):
        if int(input().strip()) in fibonacci:
            print("IsFibo")
        else:
            print("IsNotFibo")
        T -= 1

