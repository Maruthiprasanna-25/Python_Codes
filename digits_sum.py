n=int(input("enter number:"))
sum=0
temp=abs(n)
while temp>0:
    d=temp%10
    sum=sum+d
    temp//=10
print(sum)