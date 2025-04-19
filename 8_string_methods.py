#  String methods: Use built-in methods like `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.find()`, etc.



text = "I love python"
print(text.strip()) # remove spaces from both sides
print(text.rstrip()) # remove spaces from right side
print(text.lstrip()) # remove spaces from left side


print(text.find("python")) # find the index of the string
print(text.replace("python", "ruby")) # replace the old with new string