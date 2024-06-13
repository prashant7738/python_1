class student:
    def __init__(self, name , roll):
        print("New object is created")
        self.name = name
        self.roll = roll

    def info(self):
        print(f"{self.name} roll no is {self.roll}")


a = student('prashant',26)
b = student("nikesh",69)


a. info()
b. info()