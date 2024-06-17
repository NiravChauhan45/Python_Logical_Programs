# Exercise 3: Slice list into 3 equal chunks and reverse each chunk

l1 = [11,49,8,23,14,12,78,45,49]

n = 3

# for i in range(0,len(l1),n):
#     output = l1[i:i+n][::-1]
    

output = [l1[i:i+n][::-1] for i in range(0,len(l1),n)]
print(output)