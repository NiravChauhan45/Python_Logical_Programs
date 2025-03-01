# Exercise 7: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If
# not, delete it from the list

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# Expected result:--> After removing unwanted elements from list [47, 69, 76, 97]

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]

sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number = [item for item in roll_number if item in sample_dict.values()]

print(roll_number)