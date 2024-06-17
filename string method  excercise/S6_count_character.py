"""
Excercise 6 :Count the frequency of a particular character in a provided string. Eg 'hello how are you'
is the string, the frequency of h in this string is 2.
"""

# Using function
text = input("Enter The Text : ")
char = input("Enter The Character : ")

x = text.count(char)
print(f"Using Function :: frequency of searched character is {x} times")

# Without Function
count=0
for i in text:
    if i in char:
        count+=1
print(f"Without function :: frequency of searched character is {x} times")

