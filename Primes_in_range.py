def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
d=0
a=int(input())
b=int(input())
for c in range(a,b+1):
    if is_prime(c):
        d=d+1
print(d)