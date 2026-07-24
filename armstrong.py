n = int(input("enter a number: "))
s = 0
for i in str(n):
    s += int(i) ** len(str(n))
if s == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")        
