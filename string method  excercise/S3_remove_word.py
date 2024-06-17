"""
Exercise 3: Write a program to remove characters from a string starting from zero up to n and return
a new string.
"""

def remove(word,n):
    x = len(word)
    p = list(word)
    print(x,p)    

    for i in p:
        if n<=x:
            z=word[n:]
    print(z)
    
remove("nirav",2)
