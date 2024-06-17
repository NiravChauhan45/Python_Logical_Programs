# def greet(fx):
#     def mfx():
#         print("Good Morining")
#         fx()
#         print("Thanks for using this functions")
#     return mfx

# @greet   
# def hello():
#     print("hello")

# hello() 


def nirav(l):
    def pk():
      l()
    return pk


def nirav1():
    print("Hello Nirav")

nirav(nirav1)()
