a = ["Hulk","Ironman","Captain America","Ironman"]
print(a)

# to find the length of the list
print(len(a))

# to count an occurence of a particular element
print(a.count("Ironman"))

# to add to the list
a.append ("Spiderman")
print(a)

# to remove from a list
a.remove("Hulk")
print(a)
# to add to a specific location
a.insert(1,"Vision")
print(a)

# to remove from a certain location
print(a.pop(1))
print(a)

# to create a copy of list
b = a.copy()
print(b)

# to access an element
print(a.index("Ironman"))

# to entend the list
c = ["Vision","Hulk"]
a.extend(c)
print(a)

# to reverse the list
a.reverse()
print(a)

# to sort the list
a.sort
print(a)

# to clear all the data from the list
a.clear()
print(a)