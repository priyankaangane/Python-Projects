#Example 1 - Filtering and transforming data:
scores = [88,92,34,33,45,65,67]

passing = [s for s in scores if s>=50] #s ko chnage nahi karna hai
print (passing)

failing = [s for s in scores if s<50]
print(failing)

doubled = [s*2 for s in scores] #s ko change karna hai
print(doubled)

#Example 2: Sorting with a key:
students = [("Priyanka", 88), ("Arjun", 45), ("Sara", 92), ("Rohan", 38)]

by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)
# [('Sara', 92), ('Priyanka', 88), ('Arjun', 45), ('Rohan', 38)]

#Flattening a nested list
matrix = [[1,2,3],[4,5,6],[7,8]]
flat = [num for row in matrix for num in row]
flat = []
for row in matrix:
    for num in row:
        flat.append(num)

#Mistakes
lst = [1, 2, 3]
lst.append([4, 5])    # [1, 2, 3, [4, 5]] — adds the list as one item
lst.extend([4, 5])    # [1, 2, 3, 4, 5]   — adds each item individually
#2:
original = [3, 1, 2]
sorted_list = original.sort()    # sort() returns None, not the sorted list
print(sorted_list)               # None ← classic mistake

sorted_list = sorted(original)   # correct — sorted() returns a new list
#3:
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)    # skips elements silently
print(numbers)               # [1, 3, 5] — looks right but got lucky

# Safe approach — iterate over a copy or use comprehension
numbers = [n for n in numbers if n % 2 != 0]

#4
a = [1, 2, 3]
b = a             # b IS a — same object
b.append(4)
print(a)          # [1, 2, 3, 4] — surprised?



