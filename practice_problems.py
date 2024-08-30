# # Write a program for fibonacci series up to 10
# a = 0
# b = 1 
# for i in range(2,11):
#       c = a+b
#       a = b
#       b = c
#       print(c)

# # Write a program for fibonacci series using if else statement
# a = 0
# b = 1
# n = int(input("Enter the number: "))
# if n == 1:
#       print(1)
# else :
#       print(a)
#       print(b)
#       for i in range (2,n):
#             c = a+b
#             a = b
#             b = c
#             print(c)
            
# # To cheak whether the given number is prime or not
# a = int(input("Enter the number: "))
# if a <= 1:
#       print ("It is not a prime number")
# else:
#       for i in range (2,a):
#             if a % i == 0:
#                   print("The number is not prime")
#                   break
#             else:
#                   print ("The number is prime")
#                   break

# # Palindrome Number
# num = int(input("Enter the number: "))
# temp = num
# rev = 0
# while(num>0):
#       dig = num % 10
#       rev = rev * 10 + dig
#       num = num // 10
# if (rev == temp):
#       print("It is palindrome")
# else:
#       print("It is not palindrome")

            