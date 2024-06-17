import copy

mylist = [45,18,12,7]
newlist = mylist

newlist = copy.copy(mylist)
newlist[2] = 3
 
print(mylist)
print(newlist)
# print(newlist)