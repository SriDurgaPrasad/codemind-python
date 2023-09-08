a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    f=1
    while n != 0:
        r=n%10
        if r==0:
            f=0
            break
        if (i%(r)!=0):
            f=0
            break
        n=n//10
    if f==1:
        print(i,end=" ")