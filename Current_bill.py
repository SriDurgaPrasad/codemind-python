u=int(input())
if u<=199:
    b=u*1.20;
elif u>=200 and u<400:
    b=u*1.50;
elif u>=400 and u<600:
    b=u*1.80;
elif u>600:
    b=u*2.00;
if u>400:
    sc=b*15/100;
    b=b+sc;
    print(f"{b:.2f}");
else:
    sc=100;
    b=b+sc;
    print(f"{b:.2f}");