# endswith() - Return True if the string ends with thw specified value
a = "Harry Potter"
print(a.endswith("r"))
print(a.endswith("t",6,9))

# startswith() - Return True if the string starts with the specified vales
print(a.startswith("P"))
print(a.startswith("P",6,9))

# swapcase() - Swap case, lower case becomes upper case and vice versa
print(a.swapcase())

# strip() - Returns a trimmed version of the string
c = "   ***Harry Potter+++   "
print(c)
print(c.strip(" *,+, "))

# split() - Splits the string at the specified separator, and returns a list
d = "#OOFD#BRB#OMW#TB"
b = "Hello. My name is john. I am 23 years old"
print(d.split("#"))
print(b.split("."))

#ljust() - Returns a left justified version of the string
x = a.ljust(20)           #20 is nothing but the spaces
print(x,"is my favorite movie")

#rjust() - Returns a right justified version of the string
y = a.rjust(20)
print(y,"is my favorite movie")

# replace() - Returns a string where a specified value is replaced with a another specified value
e = "My name is john"
print(e.replace("john","Lisa"))

#rindex() - Searches for a specified value and returns the last position of where it was found
a1 = "Harry potter and the prisoner of Azkaban"
print(a1.rindex("prisoner"))

#rfind() - Searches for string for a specified value and retirns the last position of where it was found
a2 = "Harry potter and the Goblet of fire"
print(a2.rfind("potter"))

a3 = "bibidy bobidy boo"
print(a3.rfind("dy",6,14))  #Nothing but the range given to search that word