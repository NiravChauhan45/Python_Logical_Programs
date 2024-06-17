# Exercise 17: Remove special symbols / punctuation from a string

sentance = "/*Jon is @developer & musician"

# import re

# clean_sentance = re.sub('[A-Za-z0-9\s]',"",sentance)
# print(clean_sentance)

sta = list(sentance)
for i in sta:
    if i in "/*@&":
        print(i,end="")
