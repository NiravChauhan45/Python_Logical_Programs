# Exercise 39: Write a program to use the loop to find the factorial of a given number.

n = int(input("ENter number : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)