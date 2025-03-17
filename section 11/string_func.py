# The len() function returns the length of a string
text = "Hello, World!"
print(len(text))  # Output: 13

# Convert string to uppercase
print(text.upper())  # Output: "HELLO, WORLD!"

# Convert string to lowercase
print(text.lower())  # Output: "hello, world!"

# Convert string to title case (each word starts with a capital letter)
print("hello world".title())  # Output: "Hello World"

# Capitalize first letter of the string
print("hello world".capitalize())  # Output: "Hello world"

# Removing whitespace from the start and end of a string
text_with_spaces = "  Hello, World!  "
print(text_with_spaces.strip())  # Output: "Hello, World!"

# Removing only leading spaces
print(text_with_spaces.lstrip())  # Output: "Hello, World!  "

# Removing only trailing spaces
print(text_with_spaces.rstrip())  # Output: "  Hello, World!"

# Finding the position of a substring
text = "Hello, World!"

print(text.find("World"))  # Output: 7
print(text.index("World"))  # Output: 7

# Replacing parts of a string
text = "I love Python!"
new_text = text.replace("love", "like")
print(new_text)  # Output: "I like Python!"

# Splitting a string into a list
sentence = "Hello, how are you?"
words = sentence.split()  # Default split by space
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']

# Joining a list into a string
joined_text = " ".join(words)
print(joined_text)  # Output: "Hello, how are you?"

# Checking how a string starts or ends
text = "Python is fun"

print(text.startswith("Python"))  # Output: True
print(text.endswith("fun"))  # Output: True
print(text.endswith("boring"))  # Output: False

# Checking if a string contains only numbers
print("12345".isdigit())  # Output: True
print("123abc".isdigit())  # Output: False

# Checking if a string contains only letters
print("hello".isalpha())  # Output: True
print("hello123".isalpha())  # Output: False

# Checking if a string is alphanumeric (letters and numbers)
print("hello123".isalnum())  # Output: True
print("hello 123".isalnum())  # Output: False  # Space is not alphanumeric

# Using format()
name = "Alice"
age = 25
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is Alice and I am 25 years old."

# Using f-strings (Python 3.6+)
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Alice and I am 25 years old."

text = "banana"
print(text.count("a"))  # Output: 3
