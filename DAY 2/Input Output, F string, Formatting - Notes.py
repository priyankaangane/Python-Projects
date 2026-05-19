#Input - Output
def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

age = get_integer("Enter your age: ")

#fstrings - Number Formating
print(f"{score:.2f}")          # 88.57     — 2 decimal places
print(f"{score:.0f}")          # 89        — 0 decimal places, rounds
print(f"{100000:,}")           # 100,000   — comma as thousands separator
print(f"{0.857:.1%}")          # 85.7%     — percentage format
print(f"{42:05d}")             # 00042     — zero-padded to width 5
#Incredibly useful when debugging — you see both the name and the value without typing them separately.
x = 42
print(f"{x=}")           # x=42  — prints variable name AND value
print(f"{score=:.2f}")   # score=88.57






