n=int(input())
c=0
d=0
l=list(map(int,input().split()))
for i in range(n):
    if i%2==0:
        c+=l[i]
for i in range(n):
    if i%2!=0:
        d+=l[i]
print(abs(c-d))