def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
n=a+b+1
while 1:
    if is_prime(n):
        break
    else:
        n=n+1
print(n-a-b)