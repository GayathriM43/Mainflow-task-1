import pandas as pd
# Creating a dictionary
person = {"name": "Alice", "age": 25}
print(f"Initial dictionary: {person}")

# Adding elements to the dictionary
person["city"] = "New York"
print(f"After adding city: {person}")

# Modifying an element in the dictionary
person["age"] = 26
print(f"After modifying age: {person}")

# Removing an element using pop()
removed_age = person.pop("age")
print(f"After removing age with pop: {person}")
print(f"Removed age: {removed_age}")

# Removing an element using del
del person["city"]
print(f"After removing city with del: {person}")

# Adding elements back for further demonstration
person["age"] = 26
person["city"] = "New York"

# Removing an element using popitem()
last_item = person.popitem()
print(f"After removing last item with popitem: {person}")
print(f"Last removed item: {last_item}")