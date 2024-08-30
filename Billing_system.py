# Write a program to create a billing system at supermarket.

while True :
      name = input ("Enter customer's name: ")
      total = 0
      
      while True :
            print("Enter the quantity and the amount")
            Quantity = int(input("Enter the quantity: "))
            Amount = int(input("Enter the amount: "))
            
            total += Quantity * Amount
            repeat =input("Do you want to add more items? (yes/no): ")
            if repeat == 'no':
                  break
      print("-"*40)
      print("Name: ", name)
      print("Amount to be paid: ", total)
      print("-"*40)
      print("*******Happy Shopping*******")
      
      repeat1 = input("Do you want to go to next customer? (yes/no)")
      if repeat1 == "no":
            break 
             