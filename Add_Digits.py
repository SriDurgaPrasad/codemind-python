n=int(input())
while n>9:
    s=0
    while n!=0:
        rem=n%10
        s=s+rem
        n=n//10
    n=s
print(s)