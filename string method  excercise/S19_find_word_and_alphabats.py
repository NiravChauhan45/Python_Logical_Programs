# Exercise 19: Find words with both alphabets and numbers
str1 = "Emma253 is Data scientist50000 and AI Expert"
str2=str1.split()
new=[]
for i in str2:
 for j in i:
    if j.isdigit()==True:
        if i not in new:
             new.append(i)

print(new[:])