import pandas as pd
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(f"Initial list: {fruits}")

# Appending to the list
fruits.append("orange")
print(f"After append: {fruits}")

# Inserting into the list
fruits.insert(1, "blueberry")
print(f"After insert: {fruits}")

# Removing from the list using remove()
fruits.remove("banana")
print(f"After remove: {fruits}")

# Removing from the list using pop()
popped_fruit = fruits.pop(2)
print(f"After pop: {fruits}")
print(f"Popped fruit: {popped_fruit}")

# Updating an element in the list
fruits[1] = "kiwi"
print(f"After update: {fruits}")
