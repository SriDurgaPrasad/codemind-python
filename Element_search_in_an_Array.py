n=int(input())
l=list(map(int,input().split()))
a=int(input())
for i in l:
    if i==a:
        print(True)
        break
else:
    print(False)