# Excercise 14:# read line by line

filename = "E10_print_float.py"

with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())
        