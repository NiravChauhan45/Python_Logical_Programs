# Excercise 32: Write a program that keeps on accepting a number from the user until the
# user enters Zero. Display the sum and average of all the numbers.

n = int(input("Enter number : "))

total = 0
avg = 0
count = 0

while True:
    if n!= 0:
        total+=n
        count+=1
        avg=total/count
        n=int(input("print another number : "))
    else:
        print("Thank you")
        break
print(f"Your sum is : {total}")
print(f"Your avg is : {round(avg,2)}")