class Rectangle:
    def __init__(self, w,l):
        self.width = w
        self.length = l

    def get_area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side) #Override __init__ in Recatangle.

    def get_areaRq(self):
        return self.side * self.side

"""
1. Commnect class Square and 
sq = Square(4,4)
2. Uncommenct class Square and 
sq = Square(4)

Analyze!
"""

rc = Rectangle(16, 3)
sq = Square(5)
# calculate are of suare and rectangle
print("Rectangle: {}\nSquare with __init__ overriding {}\nSquare with defined method in the class {}".format(rc.get_area(), sq.get_area(), sq.get_areaRq()))