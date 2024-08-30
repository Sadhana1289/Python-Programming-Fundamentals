# write a program to dispaly a person's name, age and address in three different lines

Name = input("Name: ")
Age = int(input("Age: "))
Address = input("Address: ")

# Write a program to swap two variable
a = input("First variable: ")
b = input("Second Variable: ")
c=a
a=b
b=c
print("a: ",a)
print("b: ",b)

# second method
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number: "))
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("First_number: ", first_number)
print("Second_number: ",second_number)

# third method
a = 2
b =3
a,b = b,a
print(a)
print(b)

# Convert a float into integer
a = 12.5
print(int(a))

# Write a program to take an user input as interger then covert it to float
Number = int (input ("Enter the number: "))
print(type(Number))
print(float(Number))
