a,b,c,d=map(int,input().split())
if a==b or a==c or a==d or a==b+c or a==c+d or a==b+d or a==a+b+c:
    print("YES")
else:
    print("NO")