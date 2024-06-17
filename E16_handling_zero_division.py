# Excercise 16 : Let see handling zero division exceptional error


try:
    print(5/0)
except ZeroDivisionError as e:
    print(e)