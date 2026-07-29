# 5 methods of List Data Structure
List = ["apple", "orange", "banana", "strawberry", "avocado"]

# Copy the list
Copy_List = List.copy()
print("Copy of List:", Copy_List)

# Count occurrences of an item
Count_list = List.count("apple")
print("Count of 'apple':", Count_list)

# Sort list in reverse order
List.sort(reverse=True)
print("Reverse sorted List:", List)

# Clear all items from list
List.clear()
print("List after clear:", List)
print("\n######### end List Phase ##########\n")

# 2 methods of Tuple Data Structure
Tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count occurrences of an item
Tuple_Count = Tuple.count(5)
print("Count of 5:", Tuple_Count)

# Get index of first occurrence of an item
Tuple_Index = Tuple.index(8)
print("First index of 8:", Tuple_Index)
print("\n######### end Tuple Phase ##########\n")


# 5 methods of Dictionary Data Structure
Dictionary = {
    "name": "Ali",
    "age": 25,
    "city": "Tehran",
    "job": "Developer"
}

# Get value by key
user_age = Dictionary.get("age")
print("Age:", user_age)

# Get all keys
all_keys = Dictionary.keys()
print("Keys:", list(all_keys))

# Get all values
all_values = Dictionary.values()
print("Values:", list(all_values))

# Get key-value pairs
all_items = Dictionary.items()
print("Items:", list(all_items))

# Update or add items
Dictionary.update({"city": "Shiraz", "experience": 3})
print("After update:", Dictionary)

# Remove item by key
removed_job = Dictionary.pop("job")
print("Removed job:", removed_job)

# Get value or set default
email = Dictionary.setdefault("email", "info@example.com")
print("Email:", email)

# Print final dictionary
print("\nFinal Dictionary:", Dictionary)

print("\n######### end Dictionary Phase ##########\n")

# 3 methods of Set Data Structure
Set = {"apple", "banana", "cherry"}

# Add an item
Set.add("orange")
print("After add:", Set)

# Remove an item
Set.remove("banana")
print("After remove:", Set)

# Combine with another set
new_set = Set.union({"grape", "mango"})
print("Union result:", new_set)

# Print final set
print("\nFinal Set:", Set)