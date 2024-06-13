# Here in this case the value of name is accessed outside of object. SO this is public access modifier . IT is default

# class student:
#     def __init__(self,name):
#         self.name = name

# obj = student("prashant")
# print(obj.name)



# BUT in this below case it is private access as variable is declared as __ (double underscore). so in below program the value of name is not 
# accessed through outside of class. SO this is called Private access modifier



class student:
    def __init__(self,name):
        self.__name = name

obj = student("prashant")
# print(obj.__name)



# But By using _classname just infront of variable name it shows the result

print(obj._student__name)


    