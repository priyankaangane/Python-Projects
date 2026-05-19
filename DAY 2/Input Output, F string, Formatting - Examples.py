#Formatted report
students = [("Priyanka",88.5),("Arjun",89.6)]

print(f"{'Name': <12} {'Score': >6} {'Grade': >8}")
print("-" * 28)

for name,score in students:
    grade = "A" if score>85 else "B"
    print(f"{name:<12} {score: >6} {grade: >8}")
    
#Progress display of ML training
def log_epochs(epoch,total,loss,accuracy):
    print(f"[{epoch: >3}/{total}]" 
    f"Loss:{loss:.4f}"
    f"Accuracy:{accuracy:.1%}"
    
log_epoch(1, 50, 0.8734, 0.6123)
log_epoch(25, 50, 0.3421, 0.8876)
log_epoch(50, 50, 0.1205, 0.9541)
#Understanding Inputs
def get_valid_score():
    while True:
        raw = input("Enter score (0-100): ")
        if not raw.strip():
            print("Cannot be empty.")
            continue
        try:
            score = float(raw)
            if 0 <= score <= 100:
                return score
            print(f"Score must be between 0 and 100, got {score}")
        except ValueError:
            print(f"'{raw}' is not a valid number.")
            
#Strip:
name = input("Enter name: ")
if name == "":                 # user typed " " — this passes incorrectly
    print("Empty")

if not name.strip():           # correct — strips whitespace first
    print("Empty")