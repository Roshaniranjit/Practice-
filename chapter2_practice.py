# 1.Write a python program to find sum of two numbers?

from base64 import b64decode


num1 = 78
num2 = 57
sum = num1 + num2 
print("sum is:",sum)


# 2.Write a python program to find remainder when a number is divided by 2?
num1 = 20
num2 = 2
rem = num1%num2 
print("rem is:",rem)

# 3.Check the type of variable assigned using input ()function

a = int(input("Enter the number:"))
print(type(a))

# 4.Use comparison operators to find out whether a given variable a is greater than 'b' or not
# Take a =34 and b = 80

a = 34
b = 80
if a>b:
    print("Greater")
else:
    print("smaller")
    
# 5. Write a python proram to find average of two numbers entered by the user.

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
Average = a+b/2
print("The average of two mumber is:",Average)


# Write a program to calculate square of a number enter by the user 
a = int(input("Enter the number:"))
square = a**2
print("square is:",square)