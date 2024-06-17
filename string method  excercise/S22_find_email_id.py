# Exercies 22: extract all the emailid for the given string

string="Hi my name is niravchauhan753@gmail.com Govind Das and my mail id is milindmali108@gmail.com and my"

new = list(string.split())
for i in new:
   if "@" in i:
      print(i)