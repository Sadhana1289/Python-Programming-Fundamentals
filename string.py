
Name ='Hello world'
# to calculate the length of the string
print(len(Name))

# to count 
print(Name.count ('a'))

# to convert into upper case
print(Name.upper())

# to convert into lower case
print(Name.lower())

# used to capitalize the string
print(Name.capitalize())

# to find the index
print(Name.index("o",2,8))

# used to find the letter in the string
print(Name.find("l"))

# Used to replace any word from the string
print(Name.replace('e','i'))

# Used to search in the string
print('Sad' in Name) 

# to convert a string into lower case
print(Name.casefold())

# to write variable inside a string
name = 'John'
a = 'My name is {}'
print(a.format(name))

# it fills the given charcater and centralize a string
print(name.center(20,"*"))
