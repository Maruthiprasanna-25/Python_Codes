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

# This script assigns a grade based on the marks entered by the user.
# It prompts the user for their marks and prints the corresponding grade.
marks=int(input("Enter your marks: "))
if marks<50:
    print("F")
elif marks==50 or marks<60:
    print("E")
elif marks==60 or marks<70:
    print("D")
elif marks==70 or marks<80:
    print("C")
elif marks==80 or marks<90:
    print("B")
elif marks==90 or marks<=100:
    print("A")
else:
    print("Invalid marks entered.")