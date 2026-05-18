# cook your dish here
def double(value):
    if not (isinstance(value,(int,float))):
        print("Error: Unexpected Number")
        return None
    return value*2
    
print(double(3))
print(double("Hello"))



x,y=10,20
print(x,y)

x,y=y,x
print(x,y)