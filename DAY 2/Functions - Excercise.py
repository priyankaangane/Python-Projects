#Excercise 1 : Write a function describe_student(name, age, grade, is_scholarship=False) that returns a formatted summary string. If is_scholarship is True, add " — Scholarship Student" to the end. Test with:
"""
All four arguments provided
Only the first three (using default for is_scholarship)
Using keyword arguments in a different order
"""
def describe_student(name,age,grade,is_scholarship = False):
    status ="— Scholarship Student" if is_scholarship else "- Not Scholarship"
    return f"Name: {name}, Age: {age}, Grade: {grade}, Status -{status}"
    
print(describe_student("Priyanka",22,90,True))
# 2. Only first three arguments (default value used)
print(describe_student("Rahul", 20, 85))
print(describe_student(age=22,name="Som",is_scholarship=False,grade = 80))

#Excercise 2: Write a function summarize(numbers) that returns three values: the total, the average rounded to 2 decimal places, and a string "above average" or "below average" based on whether the last number in the list is above or below the average. Unpack and print all three return values.


#Excercise 3: Fix this broken function and explain in a comment what was wrong:
def make_tag(text): #shouldnt write a list in params/variales
    tags=[]
    tags.append(text)
    return tags

print(make_tag("Python"))
print(make_tag("is"))
print(make_tag("great"))