# Excercise 2 Find the reverse of a number provided by the user(any number of digit)

# num = list(input("Enter number : "))

# for i in num[::-1]:
#     print(int(i),end="")

num = int(input("Enter three digit number :-"))

a = num%10
x=num//10

b = x%10
c=x//10

if num == a**3 + b**3 + c**3:
    print("Is Armstrong")
else:
    print("Is not armstrong")