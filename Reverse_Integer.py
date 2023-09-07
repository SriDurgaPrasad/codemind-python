def rev(n):
    s=0
    while n != 0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
flag=0
if n < 0:
    n=n*-1
    flag=1
v=rev(n)
if flag==1:
    v=v*-1
print(v)