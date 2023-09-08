a,b=map(int,input().split())
m=min(a,b)
while True:
    if a%m==0 and b%m==0:
        break
    else:
        m=m-1
print(m)