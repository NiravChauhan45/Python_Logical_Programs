# Exercise 11: Find all occurrences of a substring in a given string by ignoring the case

"""
Write a program to find all occurrences of “USA” in a given string ignoring the case.
str1 = "Welcome to USA. usa awesome, isn't it?"
expected ans --> USA:-->2
"""

str1 = "Welcome to USA. usa awasome, isn't it?"

str2 = str1.upper().count("USA")
print(str2)