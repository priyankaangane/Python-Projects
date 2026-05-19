# cook your dish here
def divide(a,b):#definition function name(parameters/variables of function)
    """ Dividing two numbers a and b, returns None if B is zero """
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        return "Invalid Input"
    if b==0:
        return None
    return a/b
print(divide(4,2))

#Returning multiple values
def stats(numbers): #numbers is a list
    if not numbers:
        return None,None,None
    return sum(numbers)/len(numbers),min(numbers),max(numbers)
    
mean,minimum,maximum = stats([10,20,30,40,50])
print(f"Mean - {mean},maximum - {maximum},minimum - {minimum}")

#function callin a function
def celsius_to_fahrenheit(c):
    return (c*9/5) + 32
    
def describe_weather(temp_c):
    temp_f = celsius_to_fahrenheit(temp_c)
    condition = "hot" if temp_c>30 else "mild" if temp_c>15 else "cold"
    return f"{temp_c} C /{temp_f} F - {condition}"
    
print(describe_weather(35))    
    