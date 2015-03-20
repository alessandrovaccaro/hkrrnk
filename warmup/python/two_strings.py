if __name__ == "__main__":
    for _ in range(int(input())):
        result = False
        A = set(list(input()))
        B = set(list(input()))
        
        if len((A & B)) > 0:
            print("YES")
        else:
            print("NO")
