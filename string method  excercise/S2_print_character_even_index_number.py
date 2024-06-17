"""
 Exercise 2: Print characters from a string that are present at an even index number
"""

string=input("enter the text: ")

x = list(string)

for i in x[0::2]:
    print(i,end=" ")