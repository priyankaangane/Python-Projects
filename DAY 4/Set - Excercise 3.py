#Excersise 3:

posts = [
    ("Intro to Python", {"python", "beginner", "programming"}),
    ("Deep Learning Guide", {"python", "ai", "deep-learning"}),
    ("SQL Basics", {"sql", "database", "beginner"}),
    ("PyTorch Tutorial", {"python", "pytorch", "ai"}),
    ("Web Scraping", {"python", "scraping", "beginner"}),
]

required_tags = {"python", "ai"}
excluded_tags = {"beginner"}


# Unpacking tuple
for name, tags in posts:

    # At least one required tag is present
    atleast = len(tags & required_tags) > 0

    # None of the excluded tags are present
    no_excluded = tags.isdisjoint(excluded_tags)

    # Final condition
    if atleast and no_excluded:
        print(name)