n=int(input())
l=list(map(int,input().split()))
c=sum(l)
d=c//n
print(d in l)