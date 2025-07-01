age=int(input("enter age:"))
price=int(input("enter ticket price:"))
if age<=5 or age>=60:
    print("price:",price/2)
else:
    print("Price:",price)