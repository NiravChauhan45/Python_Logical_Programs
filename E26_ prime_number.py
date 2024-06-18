# Excercise 26:Write a program to print whether a given number is prime number or not

num =int(input("Enter Number : "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")        
    