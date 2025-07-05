n=int(input())
s=n*n
sum=0
temp=s
while temp>0:
    d=temp%10
    sum=sum+d
    temp//=10
if sum==n:
    print("Neon Number")
else:
    print("Not a Neon Number")
# n=int(input("enter a number:"))
# square=n*n
# s=str(square)
# res=sum(int(x) for x in s)
# print(res)
# if n==res:
#     print(n,"is aNeon Number")
# else:
#     print(n,"is Not a Neon Number")