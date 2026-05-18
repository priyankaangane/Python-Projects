# cook your dish here

#Datatype
name = "Priyanka"
age = 23
GPA = 8.14
print(type(name))
print(type(age))
print(type(GPA))

#Swapping
x =100
y=x #y=100
x=200
print(x) #x=200
print(y) #y=100


#isinstance
def describe_value(value):
    if(isinstance(value,int)): #standard style: if isinstance(value, int):
        print("This is a whole number")
    elif(isinstance(value,float)):
        print("This is a decimal")
    elif(isinstance(value,str)):
        print("This is a text")
    else:
        print("Unknown type")
        
print(describe_value(2))
print(describe_value(2.33))
print(describe_value("Hello"))
print(describe_value(X23))
