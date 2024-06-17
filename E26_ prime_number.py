# Excercise 26:Write a program to print whether a given number is prime number or not

def is_prime(x):
    new = []
    if x<=1:
        return False
    else:
        for i in range(1,x+1):
            if x%i==0:
                new.append(i)
    if len(new)<=2:
        return True
    else:
        return False

count = 0
num = 2

while count<25:
    if is_prime(num) == True:
        print(num,end=" ")
        count+=1
    num+=1