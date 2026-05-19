#Excercise 1: 
x = "global x"
y = "global y"

def outer():
    x = "outer x"

    def inner():
        y = "inner y"
        print(x) #"outer x"
        print(y) #"inner y"

    inner()
    print(x) #"outer x"
    print(y) #"error" --> global y

outer()
print(x) #error --> global x
print(y) #"global y"

#Excercise 2: Not using global
cart_total = 0

def add_item(price):
    global cart_total
    cart_total += price
    return cart_total

print(add_item(100))
print(add_item(250))

def add_item_fixed(price,cart_total): #thing being modified usually comes first
    cart_total += price
    return cart_total
    
total = 0
total = add_item_fixed(total,100)
print(total)
total = add_item_fixed(total,250)
print(total)

#Excercise 3: Closure call

def make_greeting(greeting):
    def whom(name):
        return f"{greeting}, {name}"
    return whom
    
englis = make_greeting("Hello")
hindi = make_greeting("Namaste")

print(englis("Priyanka"))
print(hindi("Somesh"))    






