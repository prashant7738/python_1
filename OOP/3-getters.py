class MyClass:
    def __init__ (self , value):
        self.value = value
    
    def Pvalue(self):
        print(self.value)

    @property
    def ten_value(self):
        return 10*self.value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10

    


a = MyClass(10)
# a.Pvalue()
a.ten_value = 67
print(a.ten_value)   #This is getter and it is used to access the values of an objects propertiess
a.Pvalue()

