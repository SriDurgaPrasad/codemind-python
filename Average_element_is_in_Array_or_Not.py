n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
    c+=i
avg=c//n
for i in l:
    if i==avg:
        print(True)
        break
else:
    print(False)
    