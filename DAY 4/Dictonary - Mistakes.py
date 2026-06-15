# cook your dish here
#Mistake 1 - 
d = {"name" : "Priyanka"}
print(d[age]) #keyerror
print(d.get("age",0)) #0 - safe

#Mistake 2 - Modifying dict while iterating
d = {"a":1,"b":2,"c":3}

for key in d:
    if d[key]<2:
        del d[key] #runtime error - cannot change the size during iteration
        
#Fix - iterator over copy of keys
for key in list(d.keys()):
    if d[key] <2:
        del d[key]
        
#Mistake 3 : Confusing .items(), .keys(), .values()
d = {"a": 1, "b": 2}
for x in d:           # iterates over keys only — 'a', 'b'
for x in d.values():  # iterates over values — 1, 2
for k, v in d.items() # iterates over both — ('a',1), ('b',2)