"""
Exercise 4 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character
"""

name = "nirav"

a = name[0]
# print(a)

l = len(name)
x = int(l//2)

b = name[x]
# print(b)

c= name[-1]
print(a,b,c)