# Excercise 11: Write a program to find the simple interest when the value of principle,rate of interest
# and time period is given.

P = float(input("Principle amount :: "))
R = float(input("Rate of Interest :: "))
T = int(input("For the time period :: "))

simple_interest = (P*R*T)/100
total_due = P + simple_interest
print(f"Total due amount will need to pay will be : {total_due}")