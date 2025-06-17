str=input("Enter a string: ").strip()
def is_palindrome(s):
    re=reversed(s)
    if list(s)==list(re):
        return "Palindrome"
    else:
        return "NotPalindrome"
res=is_palindrome(str)
print(res)