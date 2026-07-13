a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
d = b * b - 4 * a * c
if d > 0:
    print("roots are imaginary")
else:
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print("roots are real and different")
    print("roots are", r1, "and", r2)