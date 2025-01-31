


class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0



class Square(Shape):
    def __init__(self,length = 0):
        self.length = length
    
    def area(self):
        return self.length ** 2

obj2 = Square()
print(obj2.area())




class Rectangle(Shape):
    def __init__(self,length = 0,width = 0):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
obj3 = Rectangle(3,4)
print(obj3.area())
        