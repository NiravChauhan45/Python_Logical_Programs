# Excercise 7: Write a program that will check whether the number is armstrong number or not
"""
An Armstrong number is one whose sum of digits raised to the power three equals the
number itself. 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 =
371
"""
n = int(input("ENter three digit number : : "))

a = n%10
x = n//10
b = x%10
c = x//10

if (a**3 + b**3 + c**3) == n:
    print("This is armstrong")
else:
    print("This is not armstrong")