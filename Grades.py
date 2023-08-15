n1,n2,n3,n4,n5=map(int, input().split())
t=(n1+n2+n3+n4+n5)*100/500;
if t>=90:
    print("Grade A");
elif t>=80 and t<90:
    print("Grade B");
elif t>=70 and t<80:
    print("Grade C");
elif t>=60 and t<70:
    print("Grade D");
elif t>=40 and t<60:
    print("Grade E");
elif t<40:
    print("Grade F");