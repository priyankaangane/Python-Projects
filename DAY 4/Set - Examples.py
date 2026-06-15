# cook your dish here

# Example 1: Deduplication preserving order
def deduplicate(items):
    seen = set()   # Set initialization
    result = []    # List initialization

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result


print(deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))


# Example 2: Deduplication without preserving order
def deduplicate_set(items):
    seen = set()

    for item in items:
        seen.add(item)

    return seen


print(deduplicate_set([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))


# Example 3: Finding common and unique elements - SET OPERATIONS
python_skills = {"pandas", "numpy", "sklearn"}
job_requirements = {"pandas", "sql", "spark"}

# Skills you have that match job requirements
have = python_skills & job_requirements

# Skills required but missing
missing = job_requirements - python_skills

# Extra skills you have but are not required
extra = python_skills - job_requirements

print(f"Matching: {have}")    # {'pandas'}
print(f"Missing: {missing}")  # {'sql', 'spark'}
print(f"Extra: {extra}")      # {'numpy', 'sklearn'}


# Example 4: Fast lookup using a set
STOP_WORDS = {"the", "a", "an", "is", "it", "in"}


def remove_stop_words(text):
    words = text.lower().split()  # Fixed: lower() method call
    print(words)

    return [word for word in words if word not in STOP_WORDS]


sentence = "The model is trained on a large dataset"
print(remove_stop_words(sentence))

#output : 
[3, 1, 4, 5, 9, 2, 6]
{1, 2, 3, 4, 5, 6, 9}
Matching: {'pandas'}
Missing: {'spark', 'sql'}
Extra: {'numpy', 'sklearn'}
['the', 'model', 'is', 'trained', 'on', 'a', 'large', 'dataset']
['model', 'trained', 'on', 'large', 'dataset']