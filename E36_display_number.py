# Exercise 36: Write a program to display only those numbers from a list that satisfy the following
# conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop


num = [45,17,18,7,12,333,120,150,180,145,525,50]

for i in num:
    if i>150:
        continue
    elif i>500:
        break
    else:
        if i%5==0:
            print(i)