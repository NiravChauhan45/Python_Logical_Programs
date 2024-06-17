"""
Exercise 10: Arrange string characters such that lowercase letters should come first
"""

string = "PyNaTive"

cap = list(string.upper())
sma = list(string.lower())

new = []

l1=list(string)

for i in l1:
    if i in sma:
        new.append(i)

for i in l1:
    if i in cap:
        new.append(i)

reslut = "".join(new)
print(reslut)

