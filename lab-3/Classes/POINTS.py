class Point:
    
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        pos_x = x
        pos_y = y

    def display(self):
        print(tuple((self.x,self.y)))

    def move(self,new_x = 0,new_y = 0):
        self.x = new_x
        self.y = new_y
        pos_x = new_x
        pos_y = new_y
    
    def dist(self,to_x,to_y):
        return (((to_x - self.x) ** 2) + ((to_y - self.y) ** 2)) ** 0.5
    
obj4 = Point(2,4)
obj4.display()
obj4.move(11,15)
print(obj4.dist(5,9))