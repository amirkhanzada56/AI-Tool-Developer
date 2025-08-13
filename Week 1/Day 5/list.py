# List in python

# Creating
fruits = ["apple", "banana", "mango"]

# Access
print(fruits[1])       # apple
print(fruits[-1])      # mango

# Modify
fruits[2] = "cherry"
print(fruits)          # ['apple', 'banana', 'cherry']

# Add
fruits.append("orange")     
print(fruits)          # ['apple', 'banana', 'cherry', 'orange']

# Remove
fruits.remove("banana")     
print(fruits)           # ['apple', 'cherry', 'orange']
