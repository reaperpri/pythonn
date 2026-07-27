text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")