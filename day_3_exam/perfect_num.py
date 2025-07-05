n=int(input("enter a number:"))
sum=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j==n and i!=n:
            sum=sum+i
# print(sum)
if sum==n:
    print(n,"is Perfect number")
else:
    print(n,"is Not a perfect number")