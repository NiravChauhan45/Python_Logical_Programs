# Exercise 20: Replace each special symbol with 
# in the following string

import string

str1 = '/*Jon is @developer & musician!!'
for i in string.punctuation:
 if i in str1:
    str1=str1.replace(i,"#")

print(str1)