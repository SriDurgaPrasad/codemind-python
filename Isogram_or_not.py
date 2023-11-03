s=input()
c=[]
for i in s:
    if i not in c:
        c.append(i)
r=""
for i in c:
    r+=i
if r==s:
    print(True)
else:
    print(False)