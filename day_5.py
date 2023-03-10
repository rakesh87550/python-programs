# python strings
first_name = "Rakesh"
last_name = "Saha"

# stype casting
age = str(19)
print(first_name + " " + last_name + age)

name = "Rakesh Saha"
name += " is a good boy"
print(name)

# multiline strings
print("""
Rakesh Saha
is a 
good 
boy
# """)
      
# string methods
print("Rakesh Saha".upper())
print("Rakesh Saha".lower())
print("Rakesh Saha".title())
print("Rakesh Saha".islower())
print("RAKESH".isupper())
print(len("python programming"))
# string slicing
name = "  python programming   "
print(name[0:6])
print(name.strip())
print(name.split(" "))
print(name.replace("python", "Java"))
print(name[4])

