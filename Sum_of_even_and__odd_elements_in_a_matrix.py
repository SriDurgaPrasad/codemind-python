r,c=map(int,input().split())
mat=[]
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
even=0
odd=0
for i in mat:
    for j in i:
        if j%2==0:
            even+=j
        else:
            odd+=j
print(f"{even} {odd}")