n=int(input("enter a number:"))
if n>0:
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
else:
    n=-n
    for i in range(1,n+1):
        if i%2==0:
            print(-i,end=" ")