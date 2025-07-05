p=int(input("enter no of persons:"))
weight=map(int,input().split(" "))
s=sum(weight)
if s>500:
    print("Overload")
else:
    print("Safe")