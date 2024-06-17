# Exercise 23: Print multiplication table form 1 to 10

n = int(input("Enter number : "))

for i in range(1,11):
    print(f"{n} X {i} = {i*n}")