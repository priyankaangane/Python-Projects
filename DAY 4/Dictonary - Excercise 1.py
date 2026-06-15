# Exercise 1: Student Grade Report

classroom = {
    "Priyanka": {"math": 88, "science": 89, "english": 90},
    "Arjun": {"math": 45, "science": 67, "english": 55},
    "Sara": {"math": 92, "science": 88, "english": 95},
    "Rohan": {"math": 38, "science": 55, "english": 42},
}

def grade_report(classroom):
    for name, subjects in classroom.items():

        # Calculate average marks
        avg = round(sum(subjects.values()) / len(subjects), 2)

        # Find highest-scoring subject
        highest_subject = max(subjects, key=subjects.get)

        # Get the score of that subject
        highest_score = subjects[highest_subject]

        # Determine pass/fail status
        status = "Pass" if avg >= 50 else "Fail"

        # Display report
        print(
            f"Name: {name} | "
            f"Average: {avg} | "
            f"Highest Subject: {highest_subject} ({highest_score}) | "
            f"Status: {status}"
        )

grade_report(classroom)
