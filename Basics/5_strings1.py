# Strings can be created using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Combine multiple strings using the (+) operator (Concatenate).
# Repeat a string multiple times using the (*) operator.
# Access individual characters in a string using zero-based indexing.


hello_message1 = "Hello, my name is 'Adnan'" # Double quotes

hello_message2 = 'Hello, my name is "Adnan"' # Single quotes 

text = """I love Python 
so I'm learning it""" # Triple quotes

# Combine multiple strings using (+):
love_python = "I love Python "
learning_python = "so I'm learning it."
print(love_python + learning_python)

# Or you can use f-string:
name = "Mohammed"
age = 30
print(f"His name is {name}, and he is {age} years old.")

# You can repeat Strings multiple times using (*):
print(20*"-")

# Accessing Strings using zero-based indexing:
language = "Python"
print(language[0])
print(language[-1])
