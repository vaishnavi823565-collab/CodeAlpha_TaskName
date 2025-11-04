# Creating a Python list with different data type
a = [10,5,"SkS",2008,True]

print(a)

#Using Square Brackets
a = [78,56,85,22,43]
b = ['sudhanshu','kumar','mahi']
c = [10,'hello',3.14,True]
print(a)
print(b)
print(c)

# Using list() Constructor
a = list((2,4,7,'Sudhanshu',4.5))
print(a)

# Creating List with Repeated Elements
a = [3]*5
b = [0]*6
print(a)
print(b)

# Accessing List Elements
a = [50,40,30,20,70]
print(a[3])
print(a[-3])

# Adding Elements into List
a = []
a.append(20)
print("After append(20):",a)
a.insert(0,10)
print("After insert(0, 10)",a)
a.extend([25,30,35])
print("After extend([25,30,35])",a)

# Updating Elements into List
a = [12,14,16,18,20]
a[3] = 27
print(a)

# Removing Elements from List
a = [30,40,50,60,70]
if 25 in a:
    a.remove(25)
else:    
    print("After remove(25):",a)
popped_val = a.pop(1)
print("Popped element:",popped_val)
print("After pop(1):",a)
del a[0]
print("After del a[0]:",a)

# Iterating Over Lists to the using for loop
a = ['India','Is','My','Country']
for item in a:
    print(item)