# Excercise 19: Write a python program to search a given number from a list

n = int(input("Enter your number :: "))
l1 = [45,18,17,10,12,7]

for i in l1:
    if i == n:
        print(f"{i} in list")
        break
else:
    print("number not exists")
