#Classify EVEN/ODD
print("1. Classifying Numbers Even/Odd")
def classify_numbers(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
classify_numbers(2)
classify_numbers(3)

#Range check (Logical operator)
print("2. Range check (Logical operator)")
def valid_age(age):
    return isinstance(age,int) and (0<age<30)
    
print(valid_age(23))

#Valid roles using membership type 
print("3. Valid roles using membership type ")

roles = ["admin","ai engineer", "SDE"]

def valid_roles(role):
    if role in roles:
        return f"You have an access to {role}"
    else:
        return "You dont have an access"
        
print(valid_roles("admin"))
print(valid_roles("It support"))