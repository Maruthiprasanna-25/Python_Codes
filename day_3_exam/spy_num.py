n=int(input("enter a number:"))
sum=0
product=1
temp=n
while temp>0:
    d=temp%10
    sum=sum+d
    product=product*d
    temp//=10
if sum==product:
    print("spy number")
else:
    print("Not spy number")