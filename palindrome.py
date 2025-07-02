str=input("Enter a string: ").strip()
def is_palindrome(s):
    re=reversed(s)
    if list(s)==list(re):
        return "Palindrome"
    else:
        return "Not Palindrome"
res=is_palindrome(str)
print(res)