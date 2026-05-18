# cook your dish here
#Arithmatic Operators
x = int(input())
y = int(input())

print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x/y)
print(x**y)
print(x%y)

print(10%2==0)
print(9%2==0)

#Comparision Operators - Always returns bool
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical Operators 
age = 19
salary = 500000

print(age>18 and salary> 600000)
print(age > 18 or salary>30000)
print(not age > 18)


#identity Operators
print("Identity Operators")
a= [1,2,3]
b=[1,2,3]
c = a
print(a==b) #value is same 
print(a is b) #false 
print(a is c) #literally same object in memory?

#membership operation
print("membership operation")
fruits = ["apple","mango"]
print("apple" in fruits)

name = "priyanka"
print("somesh" in name)