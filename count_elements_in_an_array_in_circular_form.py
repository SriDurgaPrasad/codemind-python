n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2^l[(i+2)%n]%2:
        c+=1
print(c)