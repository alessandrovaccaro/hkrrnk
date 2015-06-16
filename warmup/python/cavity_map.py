#!/opt/local/bin/python3.4
def cavity(m,x):
    if x == 0 or x == (len(m)-1):
        return m[x]
    line = m[x][0]
    for i in range(1,len(m)):
        #print('value of index i %d' % i)
        if i == len(m)-1:
            line+=m[x][i] 
        elif int(m[x][i]) > int(m[x-1][i]) and int(m[x][i]) > int(m[x+1][i]) and \
            int(m[x][i]) > int(m[x][i-1]) and int(m[x][i]) > int(m[x][i+1]):
             line += 'X'
        else:
            line += m[x][i]
    return line
    
if __name__ == "__main__":
    n = int(input().strip())
    cavity_map = []
    while(n):
        cavity_map.append(input().strip())
        n -= 1
    for i in range(len(cavity_map)):
        print(cavity(cavity_map, i))
