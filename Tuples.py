a = "apple","moango","banana",1,0.51
print(type(a))

# Create single tuple
b = "Ironman",
print(type(b))

# Tuple Slicing
print(a[1:3])

# Iteration of the tuples
for i in a:
      print(i)
      
#Along with while loop
i = 0
while i < len(a):
      print(a[i])
      i+=1
      
# Conversion of the tuples
a = ("oneplus","Nokia","Redmi")
print("Before conversion",type(a))

a = list(a)
print("After conversion", type(a))
a.append("Vivo")
print(a)

a = tuple(a)
print(type(a))

# Functions in the tuples
a = ("Oneplus","Nokia","Redmi")
print(a.count("Redmi"))
print(a.index("Nokia"))