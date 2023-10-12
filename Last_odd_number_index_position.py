n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]%2!=0:
        c=i
print(c)
        