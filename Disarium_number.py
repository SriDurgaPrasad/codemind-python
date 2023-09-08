n=int(input())
s=0
t=n
l=int(len(str(n)))
while n != 0:
    r=n%10
    s=s+r**l
    l=l-1
    n=n//10
if t==s:
    print(True)
else:
    print(False)