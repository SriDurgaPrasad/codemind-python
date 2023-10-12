n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(1,len(l)):
    if i%2!=0:
        c+=l[i]
print(c)