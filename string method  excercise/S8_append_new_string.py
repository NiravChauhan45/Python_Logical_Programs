"""
Exercise 8: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""

s1="Nirav"
s2="Chauhan"

l=len(s1)
mid=l//2

f=s1[:mid]
s=s1[mid:]
s3=f+s2+s
print(s3)
