def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

select = int(input("Select an operation: "))

if select == 1:
    print("Answer =", add(a, b))
elif select == 2:
    print("Answer =", sub(a, b))
elif select == 3:
    print("Answer =", mul(a, b))
elif select == 4:
    print("Answer =", div(a, b))
else:
    print("Invalid selection")