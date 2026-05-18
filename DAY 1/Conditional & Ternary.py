#Conditional Statements - IF/ELSE/ELIF 
print("Conditional Statements - IF/ELSE/ELIF ")
print("Example 1: BMI Calculator")

def calculate_bmi(weight): #write BMI instead of weight
    if not isinstance(weight,int):
        return "Invalid Weight"
    elif (weight<18.5):
        return "Underweight"
    elif (weight < 25.0):
        return "Normal"
    elif (weight<30.0):
        return "Overweight"
    else:
        return "Obese"
print(calculate_bmi(24))
print(calculate_bmi(17))
print(calculate_bmi(50))

print("Nested Statements")
print("Example 2: Standard Nested")
def check_eligible_for_loan(age,income,credit_score):
    if age >=21:
        if income>=30000:
            if credit_score>=700:
                return "Eligible"
            else:
                return "Low credit score"
        else:
            return "Less income"
    else:
        return "Minor"
        

print("Example 2: Flatten Nested- Opp.")  
def check_eligibility(age,income,credit_score): #to check teeno variable condition hence used "if" instead of elif
    if age <21:
        return "Minor"
    if income<30000:
        return "Less income"
    if credit_score<700:
        return "Less credit_score"
    return "Eligible"
    
print(check_eligibility(22,40000,800))
    
print("Ternary in real use")
def get_label(score):
    return "Pass" if score>50 else "Fail"

score =[12,60,90,80,23]    
for s in score:
    print(get_label(s))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
