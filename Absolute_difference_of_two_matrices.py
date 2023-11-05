n=int(input())
a,b=[],[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n-1):
        print(abs(a[i][j]-b[i][j]),end=' ')
    print(abs(a[i][n-1]-b[i][n-1]))