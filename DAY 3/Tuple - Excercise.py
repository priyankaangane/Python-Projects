from collections import namedtuple
#Excercise 1: Tuples : 
    
students = [("Priyanka", 88), ("Arjun", 45), ("Sara", 92),
            ("Rohan", 38), ("Meera", 76)] #List of tuples
            
def student_summary(students):
    top_student = max(students, key = lambda x:x[1])
    bottom_student = min(students, key = lambda x:x[1])
    total = sum(score for name,score in students)
    average = round(total/len(students) ,2)
    
    return top_student,bottom_student,average

top,bottom,avg = student_summary(students)

print(f"Top Student: {top[0]} - {top[1]}")
print(f"Bottom student: {bottom[0]} — {bottom[1]}")
print(f"Class average: {avg}")

#Excercise 2 : 
t = (42)
t = (42,)
print(type((42)))
print(type((42,)))
print(isinstance((42),int))
print(isinstance((42,),tuple))

Points = namedtuple("Point", ["x","y"])

p1= Points(2,4)
p2 = Points(3,4)
p3 = Points(6,7)

print("Point 1")
print("Index access: ",p1[0],p1[1])
print("Field access: ",p1.x,p1.y)

print("Point 2")
print("Index Access ",p2[0],p2[1])
print("Field Access: ",p2.x,p2.y)

data = ["Priyanka,88,Mumbai", "Arjun,45,Delhi", "Sara,92,Bangalore"]
#Excercise 3: 
def parse_records(data):
    Student = namedtuple("Student", ["name","score","city"])
    results = []
    for items in data:
        name,score,city = items.split(",")
        results.append(Student(name,int(score),city))
        
    return results
students = parse_records(data) 
for student in students:
    print(student)
    
