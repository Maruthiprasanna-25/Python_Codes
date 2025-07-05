# n1=int(input("enter start range:"))
# n2=int(input("enter end range:"))
# if n1>0 and n2>0:
#     for i in range(n2,n1-1,-1):
#         if i%2==0:
#             print(i)
# else:
#     n1=-n1
#     n2=-n2
#     for i in range(n2,n1-1,-1):
#         if i%2==0:
#             print(-i)

# n1=int(input("enter start range:"))
# n2=int(input("enter end range:"))
# i=n2
# if n1>0 and n2>0:
#     while i<=n1:
#         if i%2==0:
#             print(i)
#         i+=1
# else:
#     n1=-n1
#     n2=-n2
#     while i<=n1:
#         if i%2==0:
#             print(i)
#         i+=1
n1 = int(input("Enter start range: "))
n2 = int(input("Enter end range: "))

# ensure the loop goes from lower to higher range
start = min(n1, n2)
end = max(n1, n2)
i = start

while i <= end:
    if i % 2 == 0:
        print(i)
    i += 1
