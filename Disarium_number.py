n=int(input())
t=n
s=0
l=int(len(str(n)))
while n:
    r=n%10
    s=s+r**l
    l=l-1
    n=n//10
if s==t:
    print(True)
else:
    print(False)
    