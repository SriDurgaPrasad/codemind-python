def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
def pre(n):
    while is_prime(n)==0:
        n=n-1
    return n
def after(n):
    while is_prime(n)==0:
        n=n+1
    return n
n=int(input())
a=n-pre(n)
b=after(n)-n
if a>b:
    print(b)
else:
    print(a)