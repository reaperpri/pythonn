import re

txt = "The rain in Spain"

# Find all occurrences of "ai"
x = re.findall("ai", txt)
print(x)

# Search for the first whitespace character
x = re.search(r"\s", txt)
print("The first white-space character is located in position:", x.start())

# Split the string at whitespace
x = re.split(r"\s", txt)
print(x)

# Replace whitespace with "9"
x = re.sub(r"\s", "9", txt)
print(x)

# Search for "ai"
x = re.search("ai", txt)
print(x)