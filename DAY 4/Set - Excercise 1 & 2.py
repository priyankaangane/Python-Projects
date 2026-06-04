#Excercise 1 - 
t1 = "the cat sat on the mat"
t2 = "the cat ate the rat"


def vocabulary_analysis(text1, text2):
    # Convert to lowercase and split into words
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    # Unique words
    vocab1 = set(words1)
    vocab2 = set(words2)

    # Set operations
    common = vocab1.intersection(vocab2)
    only_in_1 = vocab1.difference(vocab2)
    only_in_2 = vocab2.difference(vocab1)
    total_unique = len(vocab1.union(vocab2))

    # Return results in a dictionary
    return {
        "vocab1": vocab1,
        "vocab2": vocab2,
        "common": common,
        "only_in_1": only_in_1,
        "only_in_2": only_in_2,
        "total_unique": total_unique
    }


print(vocabulary_analysis(t1, t2))

#Excercise 2 - 
def deduplicate_ordered(items):
    results = []
    seen = set()
    
    for item in items:
        if not item in seen:
            seen.add(item)
            results.append(item)
            
    return results
    
print(deduplicate_ordered([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))
    
    
    
    
    
