# Exercise 13: Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"

# str2 = list(str1)

# print(str2)
total=0
count = 0
for i in str1:
    if i.isdigit()==True:
        total+=int(i)
        count+=1
print(f"""sum of digits in the given string is : {total}
avg of digits in the given string is : {count}""")