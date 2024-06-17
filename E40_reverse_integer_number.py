# Exercise 40: Reverse a given integer number

n = 678
# print(n)
# x=list(n)[::-1]
# z = int("".join(x))
# print(z)

a = n%10
x=n//10
b=x%10
c=x//10
p=f"{a}{b}{c}"
print(int(p))
