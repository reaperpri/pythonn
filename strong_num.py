n = int(input("Enter Number: "))
s = 0

for i in str(n):
    f = 1
    for j in range(1, int(i) + 1):
        f *= j
    s += f

if s == n:
    print("Strong Number")
else:
    print("Not Strong Number")