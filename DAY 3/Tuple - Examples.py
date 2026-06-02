# cook your dish here
#Example 1 - Tuple: Returning multiple values from a function:
def min_max(numbers):
    return min(numbers), max(numbers) #Tuple
    
low,high = min_max([88,55,6,77,8,90])
print(f"min = {low}, max = {high}")

#Example 2: Unpacking in a loop:
students = [("Priyanka",88),("Arjun",97),("Seema",30)] 

for name,score in students:
    grade = "Pass" if score >50 else "Fail"
    print (f"{name} : {grade}")
    
#Every time you use for name, score in zip(...) or for i, value in enumerate(...) you are unpacking tuples. 

#Example 3:  Using tuples as dict keys for a frequency map:
records = [("Math","A"),("Science","B"),("English","A"),("Math","A")] 
frequency = {}
for subject, grade in records:
    key = (subject,grade)
    frequency[key] = frequency.get(key,0)+1
    
print(frequency)

#Common Mistakes
t = (42) #this is just a int parenthesis not tuples
t = (42,) #tuples
print(type((42)))
print(type((42,)))

#Trying to modify a tuples
point = (3,7)
point[0] = 9 #typeerror : 'tuple' object does not support item assignment

#If you need to change the tuple convert to list and then change back to tuple
point = list(point)
point[0] = 10
point = tuple(point)
print(point)

#Mistake 3: 
t = ([1,2],[3,4])
t[0].append(99) #works because list inside the tuple is still mutable
print(t)

#The tuple itself cannot be changed — you cannot replace t[0] with something else. But if the tuple contains a mutable object like a list, that object can still be mutated.

#In ML, tuples represent fixed records — (image_path, label), (feature_vector, target), (train_size, val_size, test_size). Dataset items are almost always tuples. PyTorch's DataLoader returns batches as tuples of (inputs, targets). Named tuples appear in configuration objects where you want readable field names without the overhead of a full class. The (row, col) coordinate pattern using tuples as dict keys appears in graph algorithms and attention maps in transformers.