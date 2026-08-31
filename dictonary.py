# Creating a dictionary to store person details
person = {
    "name": "Alice",
    "age": 30,
    "city": "New york"
}

# Accessing the name from the dictionary
print("Name :", person["name"])

# Accessing the age from the dictionary
print("Age :", person["age"])

# Accessing the city from the dictionary
print("City :", person["city"])


# Adding a new key-value pair to the dictionary
person["Email"] = "alice@example.com"

# Printing the dictionary after adding email
print("\nAfter adding email:", person)


# Modifying the existing age value
person["age"] = 31

# Printing the dictionary after modifying age
print("\nAfter modifying age:", person)


# Removing the city from the dictionary
# pop() also returns the removed value
removed_value = person.pop("city")

# Printing the dictionary after removing city
print("\nAfter removing city:", person)

# Printing the removed value
print("Removed value:", removed_value)


# Checking whether Email exists in the dictionary
if "Email" in person:
    print("\nEmail exists in dictionary")


# Iterating over the keys of the dictionary
print("\nIterating over keys:")

# keys() returns all the keys
for key in person.keys():
    print(key)


# Iterating over the values of the dictionary
print("\nIterating over values:")

# values() returns all the values
for value in person.values():
    print(value)


# Iterating over key-value pairs
print("\nIterating over key-value pairs:")

# items() returns both key and value
for key, value in person.items():
    print(f"{key}: {value}")


# Clearing all the elements from the dictionary
person.clear()

# Printing the empty dictionary
print("\nAfter clearing:", person)