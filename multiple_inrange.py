n1=int(input())
n2=int(input())
if n1>0 and n2>0:
    for i in range(n1,n2+1):
        if i%2==0:
            print(i,end=" ")
else:
    n1=-n1
    n2=-n2
    for i in range(n1,n2+1):
        if i%2==0:
            print(i,end=" ")

    