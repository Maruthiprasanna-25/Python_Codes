age=int(input("enter your age:"))
t=(input("enter your booking time:"))
price=int(input("enter ticket price:"))
hours,minutes=map(int,t.split(":"))
time=hours + minutes / 60
if age<10:
    print("Ticket Price is:",price/2)
elif age>10:
    a=input("enter AM or PM:").lower()
    if a=="am":
        print("Price is:",price)
    elif a=="pm" and time>=10:
        print("Price is:",price+(price*(20/100)))
    elif a=="pm" and time<10:
        print("Price is:",price)

else:
    print("invalid input")