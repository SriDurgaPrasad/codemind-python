n=int(input())
ind=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        ind=i
print(ind)
        