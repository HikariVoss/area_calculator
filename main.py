import math

class Rectangle: 
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0
        self.perimeter = 0
        self.diagonal = 0
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        self.area = self.width * self.height
        return self.area
    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return self.perimeter
    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return self.diagonal
    def get_picture(self):
        string = ''
        for line in range(0, math.floor(self.height)):
            for char in range(0, math.floor(self.width)):
                string += '*'
            string += '\n'
        return string
    def get_amount_inside(self, shape):
        return math.floor(self.width / shape.width) * math.floor(self.height / shape.height)

    
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def set_side(self, side):
        self.width = side
        self.height = side
    def __repr__(self):
        return f'Square(side={self.height})'

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))