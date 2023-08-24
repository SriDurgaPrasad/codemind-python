a=int(input())
while a>9:
    s=0
    while a!=0:
        rem=a%10
        s=s+rem
        a=a//10
    a=s
print(a)
    

    