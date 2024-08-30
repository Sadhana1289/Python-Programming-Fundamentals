print("****Area Calculator****")
print('''Enter choice 1 for area of rectangle
      Enter choice 2 for arear of square
      Enter choice 3 for area of circle 
      Enter choice 4 for area of triangle''')
choice = int(input())
if choice == 1:
      length = int(input("Enter the lenght"))
      breadth = int(input("Enter the breadth"))
      area = length * breadth
      print("Area: ",area)
elif choice == 2:
      side = int(input("Enter the Side"))
      area = side * side
      print("Area od square is: ",area)
elif choice == 4:
      height = int(input("Enter the height: "))
      base = int(input("Enter the base: "))
      area = 1/2 * height * base
      print("Area of circle is : ",area)
elif choice == 3:
      radius = int(input("Enter the radius: "))
      area = 3.14 * radius *radius
      print("Area of circle is : ",area)
else:
      print("Invalid Choice")
      