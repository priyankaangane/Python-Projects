# cook your dish here
#Finding an item wth break
def find_item(students,target):
    for i,name in enumerate(students):
        if name == target:
            print(f"Found {name} at position {i}") 
            break
    else:
        print("Not found")
            
find_item(["Priyanka","Somesh","Mihika"],"Somesh")
#Building a result with a loop
def square(n):
    result=[]
    for i in range(1,n+1):
        result.append(i**2)
    return result
    
print(square(5))

#while loop
def get_valid_age():
    while True:
        age = int(input("Enter the age: "))
        if 1<=age<=120:
            return age
        print("Invalid try again")

