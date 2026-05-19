# cook your dish here
# cook your dish here
import random
import string
def get_yes_no(prompt):
    answer = input(prompt).strip().lower()
    return answer == "y"
def get_password_length():
    while True:
        try:
            length = int(input("Enter length of the password: ").strip())
            if length >= 4:
                return length
            else:
                print("Password length must be at least 4")
        except ValueError:
            print("Enter a valid number")
def build_pool(use_digits, use_symbols):
    pool = string.ascii_letters
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool
def generate_password(length, use_digits, use_symbols):
    pool = build_pool(use_digits, use_symbols)
    # Step 1 — guaranteed characters
    guaranteed = []
    # at least 2 letters
    guaranteed.extend(random.choices(string.ascii_letters, k=2))
    if use_digits:
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        guaranteed.append(random.choice(string.punctuation))
    # Step 2 — fill remaining slots
    remaining_count = length - len(guaranteed)
    remaining = random.choices(pool, k=remaining_count)
    # Step 3 — shuffle and join
    all_chars = guaranteed + remaining
    random.shuffle(all_chars)
    return "".join(all_chars)
def get_strength(use_digits, use_symbols):
    if use_digits and use_symbols:
        return "Strong"
    elif use_digits or use_symbols:
        return "Moderate"
    else:
        return "Weak"
def print_summary(password, use_digits, use_symbols):
    strength = get_strength(use_digits, use_symbols)
    print("\n" + "=" * 40)
    print(f"{'PASSWORD SUMMARY':^40}")
    print("=" * 40)
    print(f"{'Password:':<15} {password}")
    print(f"{'Length:':<15} {len(password)}")
    print(f"{'Letters:':<15} Yes")
    print(f"{'Digits:':<15} {'Yes' if use_digits else 'No'}")
    print(f"{'Symbols:':<15} {'Yes' if use_symbols else 'No'}")
    print(f"{'Strength:':<15} {strength}")
    print("="*45)
def main():
    print("=" * 40)
    print(f"{'Password Generator':^40}")
    print("=" * 40)
    length = get_password_length()
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")
    password = generate_password(length, use_digits, use_symbols)
    print_summary(password, use_digits, use_symbols)
main()