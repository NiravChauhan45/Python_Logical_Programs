# a=10
# try:
#     print(a/0)
# except Exception as e:
#     print(e)
class Student:
   def __init__(self,name):
       self.name=name
# creating a new object
stu1 = Student("Sara")
print(stu1.name)