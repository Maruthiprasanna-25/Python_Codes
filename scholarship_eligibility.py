marks=int(input("Enter your marks: "))
income=int(input("Enter your family income: "))
if marks >= 85 and 200000 >= income <= 500000:
    print("You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")