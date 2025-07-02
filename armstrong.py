n=int(input("enter a number:"))
sum=0
temp=n
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if n==sum:
    print(n,"is armstrong number")
else:
    print(n,"is not an armstrong number")