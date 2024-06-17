# Exercise 6: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

keys=["name","salary"]  

result = dict()

for k in keys:
    result.update({k:sample_dict[k]})

print(result)