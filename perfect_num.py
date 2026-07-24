n = int(input("Enter Number: "))
s = 0

for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")