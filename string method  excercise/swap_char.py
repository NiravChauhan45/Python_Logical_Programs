names='NiRav'

s=[]
for name in names:
    if name.isupper == True:    
        name.lower()
        s.append(name)
    else:
        name.upper()
        s.append(name)
        print(s)

