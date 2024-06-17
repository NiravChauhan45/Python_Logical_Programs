# Exercise 2: Write a Program to extract each digit from an integer in the reverse order.
"""
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the
digits.
"""
# Method 1
n = input("Enter three digit number :: ")
y=n[::-1]
k="".join(y)
print(int(k))


#Method 2

num = int(input("Enter three digit number :: "))

a = num %10
x = num//10
b=x%10
y=x//10
c=y%10
d=y//10

print(a,b,c,d)
