# Exercise 18: Removal all characters from a string except integers

# Method 1 
str1 = 'I am 25 years and 10 months old'
str2=list(str1)

for i in str2:
    if i.isdigit() == True:
        print(i,end="")


# Method 2
str3 =  str1.split()
new = []

for i in str3:
    if i.isdigit()==True:
        new.append(i)
print("".join(new))