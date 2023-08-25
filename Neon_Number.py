n=int(input())
s=n*n
while(s):
    r=s%10
    n=n-r
    s=s//10
if n==0:
    print("Neon Number")
else:
    print("Not Neon Number")