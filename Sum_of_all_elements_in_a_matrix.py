r,c=map(int,input().split())
m=[]
for i in range(r):
        l=list(map(int,input().split()))
        m.append(l)
d=0
for i in m:
    for j in i:
        d+=j
print(d)