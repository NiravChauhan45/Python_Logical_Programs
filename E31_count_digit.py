n = input("Enter Number : ")
x = list(n)
print(n)

count = 0

while(count<len(x)):
   for i in x:
      count+=1
print(count)