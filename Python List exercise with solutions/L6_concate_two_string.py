# Exercise 6: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

k=[i+j for i,j in zip(list1,list2)]
print(k)
    