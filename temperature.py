temp=int(input("enter the temperature in celcius:"))
if temp<0:
    print("Freezing Climate")
elif temp==0 or temp<=20:
    print("Cold Climate")
elif temp==21 or temp<=35:
    print("Warm Climate")
else:
    print("Hot Climate")
