# Excercise 1: Swap the number without using third varible

#Method 1
x = int(input("Enter the first number ::"))
y = int(input("Enter the second number ::"))

print(f"Before swaping number x:{x} and y:{y}")

x=x+y
y=x-y
x=x-y

print(f"After swaping number x:{x} and y:{y}")


# ---------------------------------------   Method 2  -------------------------------------------------


a =  int(input("Enter the first number ::"))
b = int(input("Enter the second number ::"))

a,b = b,a

print(f"After swaping number a:{a} and b:{b}")
