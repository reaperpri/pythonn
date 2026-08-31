# Initialize a list
my_list = [10, 20, 30, 40, 50]

# Print the original list
print("Original List:", my_list)

# 1. Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# 2. Slicing a list
print("Sliced List (2nd to 4th elements):", my_list[1:4])

# 3. Adding elements
my_list.append(60)
print("List after appending 60:", my_list)

my_list.insert(2, 25)
print("List after inserting 25 at index 2:", my_list)

# 4. Removing elements
my_list.remove(30)
print("List after removing 30:", my_list)

popped_element = my_list.pop()  # Removes the last element
print("List after popping last element:", my_list)
print("Popped element:", popped_element)

del my_list[1]  # Deletes the element at index 1
print("List after deleting element at index 1:", my_list)

# 5. Finding elements
index_of_40 = my_list.index(40)
print("Index of 40:", index_of_40)

count_of_40 = my_list.count(40)
print("Count of 40 in list:", count_of_40)

# 6. List concatenation
new_list = my_list + [70, 80, 90]
print("Concatenated List:", new_list)

# 7. Repeating elements
repeated_list = my_list * 2
print("Repeated List:", repeated_list)

# 8. Sorting a list
my_list.sort()
print("Sorted List:", my_list)

my_list.sort(reverse=True)
print("List sorted in descending order:", my_list)

# 9. Reversing a list
my_list.reverse()
print("Reversed List:", my_list)

# 10. Clearing the list
my_list.clear()
print("List after clearing all elements:", my_list)