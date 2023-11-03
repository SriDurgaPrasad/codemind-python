r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
a=0
b=0
for i in range(len(m)):
    if i%2==0:
        a+=sum(m[i])
    else:
        b+=sum(m[i])
print(a,b)