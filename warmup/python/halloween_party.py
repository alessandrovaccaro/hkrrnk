if __name__ == "__main__":
    T = int(input())

    while T > 0:
        T -= 1
        K = int(input())
        R = 0
        if K % 2 == 0:
            K /= 2
            R = (K*K)
        else:
            K -= 1
            K /= 2
            R = K*(K+1)
        print('%d' % R)
