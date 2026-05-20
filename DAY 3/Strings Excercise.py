#Excercise 1:
def clean_and_parse(filename):
    filename= filename.strip()
    if filename.endswith(".csv") or filename.endswith(".json"):
        if filename.endswith(".csv"):
            ext = "csv"
        else:
            ext = "json"
        parts=filename.replace(".csv" or ".json","").split("_")
        print(f"Extension:{ext},Parts:{parts}")
        return filename
    else:
        return "Unsupported filetype"
print(clean_and_parse("  sales_data_2024.csv  "))
print(clean_and_parse("user_profile.json"))
print(clean_and_parse("report.pdf"))

#Excercise 2: 
def mask_email(email):
    email = email.strip()
    if email.endswith("@gmail.com") or email.endswith("@yahoo.com"):
       name,domain = email.split("@")
       masked=email[0]+"*"*len(name) + "@" + domain
       return masked
    else:
         return "Unsupported domain"
         
print(mask_email("priyanka@gmail.com"))
print(mask_email("arjun@yahoo.com"))
        



