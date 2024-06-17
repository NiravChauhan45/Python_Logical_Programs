# Excercise 12: User will provide 2 numbers you have to find the by LCM of those 2 numbers

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if a>b:
    greater = a
else:
    greater = b

while(True):
    if (greater%a==0) and (greater%b==0):
        LCM = greater
        break
    greater+=1
print(LCM) 