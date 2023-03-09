# python operators
'''
Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
# Arithmetic operators
"""
Addition	x + y	
Subtraction	x - y	
Multiplication	x * y	
Division	x / y	
Modulus	x % y	
Exponentiation	x ** y	
Floor division	x // y
"""
print("Rakesh" + "Saha")
x = 5
y = 2
print(x // y)

# Comparison operators
"""
Equal	x == y	
Not equal	x != y	
Greater than	x > y	
Less than	x < y	
Greater than or equal to	x >= y	
Less than or equal to	x <= y
"""

# Identity operators
"""
Returns True if both variables are the same object	x is y	
Returns True if both variables are not the same object	x is not y
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)

# Membership operators
"""
Returns True if a sequence with the specified value is present in the object	x in y	
Returns True if a sequence with the specified value is not present in the object	x not in y
"""

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

