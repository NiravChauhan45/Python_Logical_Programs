# Exercise 16: Remove empty strings from a list of strings

str_list = ["nirav","","Chuahan",None,"PankajKumar"]

for i in str_list:
    if i == "" or i == None:
        str_list.remove(i)
print(str_list)