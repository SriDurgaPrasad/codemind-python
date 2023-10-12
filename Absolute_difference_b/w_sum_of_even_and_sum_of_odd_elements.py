n=int(input())
c=0
d=0
l=list(map(int,input().split()))
for i in l:
    if i%2==0:
        c+=i
for i in l:
    if i%2!=0:
        d+=i
print(abs(c-d))
