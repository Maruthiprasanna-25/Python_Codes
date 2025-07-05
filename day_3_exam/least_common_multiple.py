import math
n1,n2=map(int,input().split())
if n1>0 and n2>0:
    a=n1
    b=n2
    while b!=0:
        temp=b
        b=a%b
        a=temp
    gcd=a
    lcm=math.floor((n1*n2)/gcd)
    print(lcm)