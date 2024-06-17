"""
Exercise 9: Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and
last characters.
s1 = "America"
s2 = "Japan"
Expected output-->AJrpan
"""

s1 = "America"
s2 = "Japan"

l1 = len(s1)//2
a=s1[0]
b=s1[l1]
c=s1[-1]

l2 = len(s2)//2
x=s2[0]
y=s2[l2]
z=s2[-1]
print(a,x,b,y,c,z)
