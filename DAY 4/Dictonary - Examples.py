# cook your dish here
#DICTONARY :
#Example 1:  Configuring DICT with safe access
config = {
    "model": "xgboost",
    "learning_rate": 0.01,
    "max_depth": 6 
}

model = config.get("model","random_forest")
lr = config.get("learning_rate",0.001)
n_est= config.get("n_estimator",100) #not in config - uses default

print(f"Model: {model}, LR: {lr}, Estimator: {n_est}")

#Example 2 - Inverting a DICTONARY
label_to_id = {"cat":0,"dog":1,"bird":2}
id_to_label = {v: k for k, v in label_to_id.items()}
#OR
for k,v in label_to_id.items():
    id_to_label[v] = k
print(id_to_label)

#Example 3 - Grouping with default DICTONARY:
from collections import defaultdict

students = [
    ("Priyanka", "A"),("Arjun","B"),("Sara", "A"),("Dev","D")
]

by_grade = defaultdict(list)
for name, grade in students:
    by_grade [grade].append(name)
    
for grade,names in sorted(by_grade.items()):
    print(f"Grade{grade}: {', '.join(names)}")
    
    










