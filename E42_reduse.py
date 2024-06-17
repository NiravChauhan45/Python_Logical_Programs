# Excercise 42: write logic to know whethe given number is perfect number or not

from functools import reduce

n = 28

li = []

for i in range(1,n+1):
    if n%i==0:
        li.append(i)

# def mysum(x,y):
#     return x+y

result = reduce(lambda x,y:x+y,li)
print(result)
if n==result:
    print("Perfect number")
else:
    print("Not perfect number")