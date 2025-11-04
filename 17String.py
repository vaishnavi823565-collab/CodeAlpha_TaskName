s = "SKS"


print(s[1])

s1 = s+s[0]

print(s1)


# Creating a String
# Strings can be created using either single (') or double (") quotes.


s1 = 'SKS'

s2 = "SKS"

print(s1)

print(s2)

# Multi-line Strings
# If we need a string to span multiple lines then we can use triple quotes (''' or """).

s = """I am going to computer lab"""
print(s)
s = "'I'm a Geek"""
print(s)
a="Sudhanshu kumar,Branch :- CSE Roll no :- 33\CSE\2025,"
print(len(a))


s1 = "Hello"
s2 = "Sudhanshu"
s3 = s1+""+s2
print(s3)


s = "Hello Sudhanshu Bro,"

print(s*3)


name = "Sudhanshu"
age = 17
print(f"Name:{name},Age:{age}")



s = "My name is {} and I am {} years odd.".format("Sudhanshu",17)
print(s)



x = ("apple","bana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

