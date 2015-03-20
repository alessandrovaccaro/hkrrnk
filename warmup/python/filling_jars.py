if __name__ == "__main__":
    jars, oper = [int(x) for x in input().split(' ')]
    candies = 0

    for i in range(oper):
        op = [int(i) for i in list(input().split(' '))]
        candies += (((op[1]+1) - op[0]) * op[2])
    print("%d" % (candies/jars))
