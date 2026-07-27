def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter a number to generate: "))
f =[fib(i) for i in range(n)]
print(f"the first {n} numbers in fibnoacci series are: {f}")
check = int(input("Enter a number to check: "))
if check in f:
    print(f"{check} is in the Fibonacci series.")
else:
    print(f"{check} is not in the Fibonacci series.")
