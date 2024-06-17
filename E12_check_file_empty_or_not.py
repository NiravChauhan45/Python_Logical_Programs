# Exercise 12: Check file is empty or not,Write a program to check if the given file is empty or not

import os
size = os.stat("E10_print_float.py").st_size

if size == 0:
    print("file is empty")
else:
    print("file is not empty")
