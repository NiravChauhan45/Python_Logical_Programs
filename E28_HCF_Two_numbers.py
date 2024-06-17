# Excercise 28: User will provide 2 numbers you have to find the HCF of those 2 numbers

x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))

x_div = []
y_div = []

for i in range(1,x+1):
    if x%i==0:
        x_div.append(i)
print(x_div)
for i in range(1,y+1):
    if y%i==0:
        y_div.append(i)
print(y_div)

comman_list = []
for i in x_div:
    if i in y_div:
        comman_list.append(i)

print(f"HCF of given number is : {max(comman_list)}")

