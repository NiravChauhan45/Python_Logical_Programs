# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first
# set

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# Intersection is {57, 83, 29}
# First Set after removing common element {65, 42, 78, 23}

a = first_set.intersection(second_set)
print(a)

for i in a:
    first_set.remove(i)
print(first_set)