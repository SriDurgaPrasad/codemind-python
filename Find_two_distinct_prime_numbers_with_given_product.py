def is_prime(n):
    if n<=1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(2,n):
    if is_prime(i) and is_prime(n//i) and i*(n//i)==n:
        print(i,n//i,end=" ")
        break;
else:
    print(-1)