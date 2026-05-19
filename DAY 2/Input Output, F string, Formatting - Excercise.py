#Excercise 1
def get_valid_age():
    while True:
        age_input = input("Enter an age: ")

        # Check empty or whitespace-only input
        if not age_input.strip():
            print("Cannot be empty")
            continue

        try:
            age = int(age_input)

            if 1 <= age <= 120:
                return age

            print(f"Age must be between 1 and 120, got {age}")

        except ValueError:
            print(f"'{age_input}' is not a valid number.")


items = [
    ("Neural Networks", 4, 2499.00),
    ("Python Basics", 12, 399.00),
    ("Data Structures", 7, 899.50),
    ("Deep Learning", 2, 3299.00),
]

print(f"{'Course':<20} {'Qty':>6} {'Price':>10} {'Total':>12}")
print("-"*45)
grand_total =0
for course,qty,price in items:
    total = qty*price 
    grand_total +=total
    print(f"{course:<20}{qty:>6}{price:>10.2f}{total:>12.2f}")

print("-"*45)

print(f"{'Grand Total: ':>38} {grand_total:>10.2f}")


#Excercise 3: 
pi = 3.14159265
population = 1428627663
ratio = 0.734521
score = 42

print(f"{pi:.3f}") #3.141 
print(f"{population:,}") #poppulation, 
print(f"{ratio:.2%}") #
print(f"{score:08d}") #00000008
print(f"{'Python':<10}|{'AI':>10}") #Python |    AI