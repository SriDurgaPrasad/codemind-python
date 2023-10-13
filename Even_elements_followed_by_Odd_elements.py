n=int(input())
l=list(map(int,input().split()))
m=[]
n=[]
for i in l:
    if i%2==0:
        m.append(i)
    else:
        n.append(i)
print(*(m+n))