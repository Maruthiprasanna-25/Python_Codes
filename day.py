# This program takes a number from 1 to 7 and prints the corresponding day of the week.
# If the number is not in this range, it prints an error message.
n=int(input("Enter a number: "))
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
elif n==7:
    print("Sunday")
else:
    print("Invalid input, please enter a number between 1 and 7.")