# Exercise 8: Concatenate two lists in the following order

# Expected result:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

kl=[]
for i in list1:
    for j in list2:
        kl.append(i+j)
print(kl)