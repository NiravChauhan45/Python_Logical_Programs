# Excercise 30:print following pattern

# 1
# 22
# 333
# 4444
# 55555

n=int(input("Enter number : "))

for i in range(0,n+1):
    for j in range(0,i):
        print(i,end="")
    print("\n")