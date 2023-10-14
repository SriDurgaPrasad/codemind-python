n=int(input())
l=list(map(int,input().split()))
z=0
c=sum(l)
d=c//n
for i in l:
    if i >=d:
        z+=1
print(z)
