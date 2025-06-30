# This script demonstrates the use of a simple condition in Python.
# It checks if a condition is true and prints a message accordingly.
if 1<2:
    print("This is a true condition.")



# This script checks if a number is eligible to vote based on age.
# It prompts the user for their age and prints whether they are eligible to vote or not
n=int(input("Enter a number: "))
if n<18:
    print("You are a minor,not eligible to vote.")
else:
    print("eligible to vote.")



# This script categorizes a person based on their age.
# It prompts the user for their age and prints the corresponding category.
#used to check more than one condition
n=int(input("Enter a number: "))
if n<10:
    print("child")
elif n<20:
    print("teenager")
elif n<30:
    print("young adult")
elif n<40:
    print("adult")
else:
    print("senior citizen")