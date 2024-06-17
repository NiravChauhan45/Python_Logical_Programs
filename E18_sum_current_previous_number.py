"""
Excercise 18 : Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and
previous number.
Expected result: 0,1,3,5,7,9,11,13,15,17
"""
prev_num = 0

for i in range(1,11):
    x=i+prev_num
    prev_num=i
    print(x,end=" ")