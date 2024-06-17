# class MyClass:
#     def __init__(self,value) -> None:
#         self._value=value
    
#     def show(self):
#         print(f"Value is {self._value}")

# # get data using getter
#     @property
#     def ten_value(self):
#         return 10 * self._value

# # set data using setter
#     @ten_value.setter
#     def ten_value(self,new_value):
#         self._value = new_value/10
         
# obj = MyClass(10)
# obj.show()
# obj.ten_value=100
# print(obj.ten_value)
# obj.show()

class MyClass:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
    
obj = MyClass(10)
print(obj.value)
