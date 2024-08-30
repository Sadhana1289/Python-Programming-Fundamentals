# Write a program to seperate the following string into coma seperated values
a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
print(a.replace(".",","))

# Write a program to sort a string alphabetically in python
print(sorted(a))

# Write a program to remove character from a string
print(a.replace("Y","P"))

# Write a program to cheak number of occurence of a substring in a string
a = "HI HELLO HOW ARE YOU...!!!"
print(a.count("H"))

# Take an input from a user as astring then, reverse it
a = "Hello John"
print(a[::-1])

# Wrtite a program to cheak if a string contain only digits
a = input("Enter the string: ")
print(a.isdigit())

# Write a program to check if a string is palindrome
a = input("Enter the string: ")
rev = a[::-1]
if a == rev:
      print("It is palindrome")
else: 
      print("It is not palindrome")

# Write a program to find number of vowels in the string
a = input("Enter the string: ")
vowels = 0
for i in a:
      if i == 'a' or i == 'e' or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "O" or i == "I" or i == "U":
            vowels+=1
print("The number of vowels in the string are",vowels)

# Write a program to check if every word in a string begins with a capital letter
a = input("Enter the string: ")
print(a.istitle())