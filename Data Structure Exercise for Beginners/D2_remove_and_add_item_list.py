# Exercise 2: Remove and add item in a list

"""
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the
list.
sample_list = [34, 54, 67, 89, 11, 43, 94]
List After removing element at index 4 [34, 54, 67, 89, 43, 94]
List after Adding element at index 2 [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last [34, 54, 11, 67, 89, 43, 94, 11]
"""

list1 = [34, 54, 67, 89, 11, 43, 94]

list1.pop(4)
print(f"List After removing element at index 4 : {list1}")
list1.insert(2,11)
print(f"List after Adding element at index 2 : {list1}")
list1.append(11)
print(f"List after Adding element at last : {list1}")