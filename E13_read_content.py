# Excercise 13:read content from the file

filename = "E12_check_file_empty_or_not.py"

with open(filename) as f_obj:
    content = f_obj.read()
print(content)