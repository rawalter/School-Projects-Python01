#Exercise: 15.19
#By: Robert A. Walters
#Created on: 2/19/16
#Program Description: decimal to binary

def decimalToBinary(value):
   #Function to print binary number for the input decimal using recursion
        if value > 1:
                decimalToBinary(value//2)
        print(value % 2,end = '')

# Take decimal number from user
dec = int(input("Enter a positive integer greater than 1: "))
decimalToBinary(dec)
print("<-----The binary is")
#Credit to programiz