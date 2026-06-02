from collections import namedtuple

data = [
    "Asha,75000,Engineering",
    "Rahul,52000,Marketing",
    "Neha,91000,Engineering",
    "Karan,48000,Sales",
    "Isha,68000,Marketing"
]

def employee_summary(data):
    # Defined fields with consistent lowercase style for standard python attributes
    Employee = namedtuple("Employee", ["name", "salary", "department"])
    records = []
    
    for items in data:
        name, salary, dept = items.split(",")
        records.append(Employee(name, int(salary), dept))
        
    # Using the named attributes (.salary) instead of indices
    highest_salary = max(records, key=lambda x: x.salary)
    lowest_salary = min(records, key=lambda x: x.salary)
    
    # Corrected sum() usage
    total = sum(x.salary for x in records)
    
    # Corrected parentheses for round()
    average = round(total / len(records), 2)
    
    # Returning all 4 elements
    return records, highest_salary, lowest_salary, average

# Properly unpacking all 4 returned items
records, highest, lowest, average = employee_summary(data)    

# Displaying the summary data cleanly
print("--- Employee Records ---")
for person in records:
    print(f"{person.name} works in {person.department} and earns {person.salary}")

print("\n--- Financial Insights ---")
print(f"Highest Salary: {highest.name} ({highest.salary})")
print(f"Lowest Salary: {lowest.name} ({lowest.salary})")
print(f"Average Salary: {average}")