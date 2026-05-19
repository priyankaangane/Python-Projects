#Excercise 1 - Sum of even using for loop
def sum_of_evens(n):
    sum = 0 
    for i in range(1,n+1):
        if i%2==0:
            sum = sum + i 
        else:
            continue
    return sum
print(sum_of_evens(5))

#Excercise 1 - Sum of even using while loop
def sumof_evens(n):
    sum = 0
    i = 1
    while i<n:
        if i%2==0:
            sum = sum+i 
        i=i+1
    return sum
        
print(sumof_evens(5))


#Exercise 2 Given this data: Write a loop using zip() and enumerate() together that prints:

students = ["Priyanka", "Arjun", "Sara", "Rohan", "Meera"]
scores   = [88, 45, 92, 38, 76]

def results(students,scores):
    for student,score in zip(students,scores):
        if score>=50:
            result ="Pass"
        else:
            result= "Fail"
        print (f"{student} - {score} - {result}")
        
        
results(students,scores)
#OR : for i, (student, score) in enumerate(zip(students, scores), start=1):
    #result = "Pass" if score >= 50 else "Fail"

#print(f"{i}. {student} - {score} - {result}")


#Excercise 3 Write a function first_negative(numbers) that takes a list of numbers and returns the first negative number it finds. If there are no negatives, return None. Use break to stop as soon as you find one. 

def first_negative(numbers):
    #numbers = []
    
    for i in numbers:
        if i<0:
            return i 
            break
        else:
            continue
print(first_negative([3, 7, -2, 5, -8])) 
print(first_negative([1, 2, 3, 4])) 
    
    
    
    
    
    
    
    
    
    
    
    
    