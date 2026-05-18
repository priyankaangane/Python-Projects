print("Exercise 1:")

def ticket_price(age, is_student):

    if not isinstance(age, int):
        return "NA"

    if age < 5:
        return "Free"

    elif 5 <= age <= 12:
        return "Rs.100"

    elif 13 <= age <= 17:
        return "Rs.150"

    elif age >= 18 and is_student:
        return "Rs.200"

    else:
        return "Rs.300"


# Test cases
print(ticket_price(4, False))     # Free
print(ticket_price(10, False))    # Rs.100
print(ticket_price(15, False))    # Rs.150
print(ticket_price(18, True))     # Rs.200
print(ticket_price(18, False))    # Rs.300

#nested conditions
print("Exercise 2:")
def process_data(data):
    if data is None:
        return "No data"
    if not isinstance(data,list):
        return "Not in a List"
    if len(data)==0:
        return "Empty List"
    return f"Processing {len(data)} items"
     
number =[1,2,3,4]  
print(process_data(number))



print("Exercise 3:")

x = 200
result1 = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(result1)

lists = [1, 2, 3]
result2 = "has items" if len(lists) != 0 else "empty"
print(result2)

username = "Priyanka"
result3 = "guest" if username == "" else username
print(result3)









