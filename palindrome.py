def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        print(n,"is palindrome")
    else:
        print(n,"is not palindrome")
n=int(input("Number"))
is_palindrome(n)
