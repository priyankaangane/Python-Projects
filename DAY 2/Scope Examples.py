# cook your dish here
x = "global"
def outer():
    global x
    x = "enclosing"
    
    def inner():
        
        x = "local"
        print(x)
        
    inner()
    print(x)
    
outer()
print(x)

#Example 3 : Closure remembering state
def make_multiplier(factor):
    def multiply(number):
        return number * factor    # factor from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))     # 10
print(triple(5))     # 15
print(double(9))     # 18