def rev(n):
    s=0
    while n != 0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
n=int(input())
v=rev(n)
print(v)