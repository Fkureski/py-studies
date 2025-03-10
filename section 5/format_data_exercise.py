# Multiple inputs in the same line

data = input('Write your name and age:').split() 

name = data[0]
age = data[1]

print(f'I am {name.upper()}, and I have {age} years old')