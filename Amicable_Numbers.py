def count(a,b):
    s=0
    p=0
    for i in range(1,max(a,b)):
        if a%i==0 and i!=a:
            s=s+i
        if b%i==0 and i!=b:
            p=p+i
    if s==b and p==a:
        print("Amicable")
    else:
        print("Not Amicable")
a=int(input())
b=int(input())
count(a,b)
    