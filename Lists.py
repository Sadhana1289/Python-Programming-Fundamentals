# Iteration using for loop
a = ["Hulk","Ironman","Captain America"]
for i in a:
      print(i)
      
# Iteration using for loop with range and length function
for i in range(len(a)):
      print(a[i])
      
# Iteration using while loop
i = 0
while i<len(a):
      print(a[i])
      i +=1
      
# Short - Hand for loop
[print(a[i]) for i in range (len(a))]