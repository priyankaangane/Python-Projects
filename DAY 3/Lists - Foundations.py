# cook your dish here
fruits = ["apple", "mango", "banana"]

print("Original list:", fruits)

# Sort in ascending order
fruits.sort()
print("After fruits.sort():", fruits)

# Create a new sorted list
sorted_fruits = sorted(fruits)
print("sorted(fruits):", sorted_fruits)

# Sort in descending order
fruits.sort(reverse=True)
print("Descending order:", fruits)

# Sort by string length
fruits.sort(key=len)
print("Sorted by length:", fruits)