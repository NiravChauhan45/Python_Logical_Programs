# Exercise 4: Count the occurrence of each element from a list

"""
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to
show the count of each element.
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Output:--> Printing count of each item {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""

list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count=dict()

for i in list1:
 if i in count:
    count[i]+=1
 else:
    count[i]=1

print(count)