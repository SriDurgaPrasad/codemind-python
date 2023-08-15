a,b,c=map(int, input().split())
if a==b and b==c and c==a:
    print("Equilateral triangle");
elif a!=b and b!=c and c!=a:
    print("Scalene triangle");
else:
    print("Isosceles triangle");