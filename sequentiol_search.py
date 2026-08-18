def sequential_search(list1, n, key):
    for i in range(0, n):
        if list1[i] == key:  # Uses correct variable index 'i'
            return i
    return -1  # Placed outside the loop

list1 = [1, 3, 5, 4, 7, 9, 12]
print("list1 =", list1)

# Safe conversion to integer instead of eval()
key = int(input("Enter the element to find: "))
n = len(list1)
res = sequential_search(list1, n, key)

if res == -1:
    print("Element not found") 
else:
    print("Element found at index:", res)
