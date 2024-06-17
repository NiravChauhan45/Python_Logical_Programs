# MAP
l = [1,1,2,4,6,4,3]

newl = set(map(lambda x:x**x,l))
print(newl)

new = set(filter(lambda x:x%2==0,l))
print(new)