# cook your dish here
# SETS - Common Mistakes


# Mistake 1: Creating an empty set
s = {}          # This creates a dictionary, NOT a set
s = set()       # Correct way to create an empty set

print(type({}))      # <class 'dict'>
print(type(set()))   # <class 'set'>


# Mistake 2: Trying to access set elements using indexing
s = {3, 1, 4, 1, 5, 9}

# print(s[0])  
# TypeError: 'set' object is not subscriptable
# Sets are unordered and do not support indexing

for item in s:
    print(item)  
# Works, but order is not guaranteed


# Mistake 3: remove() vs discard()
s = {1, 2, 3}

# s.remove(99)
# KeyError: 99
# remove() throws an error if element is not found

s.discard(99)
# No error
# discard() safely removes an item if it exists