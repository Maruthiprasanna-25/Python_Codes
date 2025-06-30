# This is the efficient method to take input in a list
# and convert it to integers
lst=list(map(int,input().split()))
print(lst)
## This is the inefficient method to take input in a list
# and convert it to integers
lst1=input().split()
print(lst1)
lst2=map(int,lst1)
print(list(lst2))
lst3=list(lst2)
print(lst3)

a,b=list(map(int,input().split()))
print(a,end=" ")
print(b)