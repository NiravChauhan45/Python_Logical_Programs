"""
Exercise 22: Calculate income tax for the given income by adhering to the below rules
first 10k--> 0%
second 10 --> 10%
remaining-->20%

Expected Output :For example, suppose the taxable income is 45000 the income tax payable is
100000% + 1000010% + 25000*20% = $6000.
"""

n = int(input("enter the number:"))

if n <= 10000:
    print(n)
else:
    a = n - 10000
    b = a - 10000
    c = b * 0.2
    d = c + 1000
    
    print(d)

# Another way of doing the same
n=int(input("enter the number: "))
a=10000
b=10000
c=n-(a+b)
tax=0
if n<=a:
 tax=0
elif n>a and n<20000:
 tax=b*0.1
else:
 tax=(b*0.1)+(c*0.2)

print(tax)