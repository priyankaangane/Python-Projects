print("1. Logical Operators")
def is_eligible_to_vote(age,is_citizen):
    return isinstance(age,int) and (age>=18) and (is_citizen == True) #just write is_citizen
    
print(is_eligible_to_vote(20,True))
print(is_eligible_to_vote(18,False))
print(is_eligible_to_vote(17,False))
print(is_eligible_to_vote(17,True))

print("2. Arithematic Operators")
def categorize_score(score):
    if not isinstance(score, int):
        return "Invalid Number"
    elif score >= 75:
        return "Distinction"
    elif score >= 60:
        return "First Class"
    elif score >= 50:
        return "Second Class"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


scores = [90, 72, 55, 42, 30]

for s in scores:
    print(categorize_score(s))
    
    
print("Excercise 3")
print(10 % 3) # False -->1
print(2 ** 4) #16
print(10 // 3) # 3.3 --> 3 
print(5 or 0) #5 
print(0 or "fallback") # fallback
print([] or "empty") #empty
print("hello" and "world") #hello --> world
print(not not True) #true