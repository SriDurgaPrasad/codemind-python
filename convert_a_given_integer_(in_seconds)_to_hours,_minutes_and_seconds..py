n=int(input())
h=n/3600
m=(n%3600)/60
s=(n%3600)%60
print("H:M:S-%d:%d:%d"%(h,m,s))
