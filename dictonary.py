person = {
    "name": "Alice",
    "age" : 30,
    "city" : "New york"
}
print("Name :", person["name"])
print("Age :", person["age"])
print ("City :", person["city"])
person["Email"] = "alice@example.com"
print("\nAfter adding email:", person)
person["age"] = 31
print("\nAfter modifying age:", person)
removed_value = person.pop("city") 
print("\nAfter removing city:", person) 
print("Removed value:", removed_value)
if "Email" in person:
 	print("\nEmail exists in dictionary")
print("\nIterating over keys:") 
for key in person.values():
 	print(key) 
print("\nIterating over values:") 
for value in person.values():
 	print(value)
print("\nIterating over key-value pairs:") 
for key, value in person.items():
 	print(f"{key}: {value}")
#clear
person.clear()	
print("\n After clearing ", person) 	 