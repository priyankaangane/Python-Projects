#Excercise 1 - updated :
classroom = {
    "Priyanka": {"math": 88, "science": 92, "english": 76},
    "Arjun":    {"math": 45, "science": 67, "english": 55},
    "Sara":     {"math": 92, "science": 88, "english": 95},
    "Rohan":    {"math": 38, "science": 55, "english": 42},
}
def grade_report(classroom):
    report = {}
    for name, subjects in classroom.items():
        avg = round(sum(subjects.values()) / len(subjects), 2)
        highest_subject = max(subjects, key=subjects.get)
        status = "Pass" if avg >= 50 else "Fail"

        report[name] = {
            "average": avg,
            "highest_subject": highest_subject,
            "status": status
        }
    return report
#Excercise 2  - Count Frequency using Counter
from collections import Counter, defaultdict

def word_frequency(text):
    words = text.lower().split()
    words = [word.strip(".,!?;:") for word in words]
    count = Counter(words)
    return count.most_common(5)

word_frequency("Python is a powerful programming language. Python is easy to learn and Python is widely used in data science, web development, and automation. Learning Python helps you build real-world applications.")

#Excercise 3: 
d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
def invert_and_group(d):
    group = defaultdict(list)
    for key, value in d.items():
        group[value].append(key)
    return dict(group)
        
invert_and_group(d)












