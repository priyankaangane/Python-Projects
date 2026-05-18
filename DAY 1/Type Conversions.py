# cook your dish here
#Excercise 1
birth_year=input()
birth_year_int = int(birth_year)

#calculate age 
age = 2025 - birth_year_int
print(f"You are {age} years old")

#Excercise 2
def safe_divide(a,b):
    if result is not None:
        return a/b 
    else:
        return None 
    
result = safe_divide(0,5)
#falsy check
if result is not None:
    print(result)
else:
    print("Cannot divide by zero")

result = safe_divide(15,5)
if result is not None:
    print(result)
else:
    print("Cannot divide by zero")
result = safe_divide(10,0)    
if result is not None:
    print(result)
else:
    print("Cannot divide by zero")
    
    
    
#Excercise 3
print(bool(0)) #False 
print(bool("")) #False 
print(bool(" ")) #False --> True
print(bool(None)) #True -->False
print(bool([]))  #True -->False
print(int(True)) #1
print(int(False)) #2 -->0
print(True + True + True) #3

