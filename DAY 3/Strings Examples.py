# cook your dish here
#Example 1 : Strings: Cleaning messy user input:
def clean_input(raw):
    return raw.strip().lower().replace(" ","_")
    
print(clean_input(" Machine Learning"))
print(clean_input("  Deep  Learning  "))

#Example 2:Checking and parsing a filename:
filename="report_2024_final.csv"
if filename.endswith(".csv"):
    parts = filename.replace(".csv","").split("_")
    print(parts)
    print(parts[0])
    print(parts[1])

#Example 3: Reversing and palindrome check:
def ispalindrome(word):
    cleaned = word.strip().lower()
    return cleaned == cleaned [::-1] #cleaned = word & cleaned[::1] word ka ulta
    
print(ispalindrome("racecar"))
print(ispalindrome("Madam"))
print(ispalindrome("Python"))


#Mistakes to avoid
name ="priyanka"
name.upper()
print(name)
name = name.upper()
print(name)

#2: Confusing find() and index() - Use find() when the substring might not exist. Use index() only when you are certain it is there.
s = "hello"
s.find("z") # returns -1 no value found
s.index("z") #ValueError: substring not found

#3: String concatenation in a loop 
#SLOW
result =""
for word in words:
    result +=word
#FAST
"--".join(words)