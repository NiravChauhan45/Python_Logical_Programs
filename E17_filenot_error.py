# Excercise 17 : write a program to check file is exists or not

filename="saddo.txt"

try:
    with open(filename) as fp:
        content = fp.read()
    print(content)

except Exception as e:
    print(e)