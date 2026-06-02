# Exercise 1:
def clean_and_parse(filename):
    filename = filename.strip()

    if filename.endswith(".csv") or filename.endswith(".json"):
        ext = "csv" if filename.endswith(".csv") else "json"
        parts = filename.replace("." + ext, "").split("_")

        return {
            "Extensions" : ext,
            "Parts" : parts
        }

    else:
        return "Unsupported filetype"


print(clean_and_parse("  sales_data_2024.csv  "))
print(clean_and_parse("user_profile.json"))
print(clean_and_parse("report.pdf"))


# Exercise 2:
def mask_email(email):
    email = email.strip()

    if "@" not in email:
        return "Invalid email"

    name, domain = email.split("@")

    # supported domains
    if domain in ["gmail.com", "yahoo.com"]:
        masked = name[0] + "*" * (len(name) - 1) + "@" + domain
        return masked
    else:
        return "Unsupported domain"


print(mask_email("priyanka@gmail.com"))
print(mask_email("arjun@yahoo.com"))


# Exercise 3:
def word_stats(sentence):
    words = sentence.split()
    i = 0
    word_count = 0
    longest_word = ""

    while i < len(words):
        word_count += 1

        if len(words[i]) > len(longest_word):
            longest_word = words[i]

        i += 1

    cleaned = sentence.replace(" ", "").lower()
    count = len(cleaned)
    is_palindrome = cleaned == cleaned[::-1]

    return {
        "char_count": count,
        "is_palindrome": is_palindrome,
        "word_count": word_count,
        "longest_word": longest_word
    }


print(word_stats("Never odd or even"))