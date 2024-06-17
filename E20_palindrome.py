# Exercise 20:Write a program to check if the given number is a palindrome number

num = input("Enter three digit number :: ")

a = num[::-1]
print(a)
if num==a:
    print(f"{num} this is palindrome number!")
else:
    print(f"{num} this is not palindrome number!")