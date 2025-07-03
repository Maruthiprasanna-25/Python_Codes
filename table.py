n=int(input("enter a number:"))
if n>0:
    for i in range(1,11):
        r=n*i
        print(n,"*",i,"=",r)
else:
    n=-n
    for i in range(1,11):
        r=n*i
        print(-n,"*",i,"=",-r)
