# Exercise 38: Display Fibonacci series up to 10 terms

n = 0
n1 = 1

print(n,end=" ")
print(n1,end=" ")
for i in range(0,10):
    num = n+n1
    n=n1
    n1=num

    print(num,end=" ")