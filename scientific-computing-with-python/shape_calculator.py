from math import floor

class Rectangle:
    width = 0
    height = 0
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_dim(self):
        return "Width: " + str(self.width) + ", Height: " + str(self.height)
        
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
        
    def get_perimeter(self):
        return 2 * (self.width + self.height)
        
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        str = ""
        
        if self.width > 50 or self.height > 50:
            return "Too big for picture"
            
        for h in range(self.height):
            for w in range(self.width):
                str += "*"
            str += "\n"
        
        return str
        
        
    def get_amount_inside(self, shape):
            return floor(self.get_area() / shape.get_area())
            
            
    def __str__(self):
        return "Rectangle(width="+ str(self.width) + ", height="+ str(self.height) + ")"
            
            
        

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = self.height = side
        
    def set_side(self, side):
        self.width = self.height = side
        
    def set_width(self, side):
        self.set_side(side)
        
    def set_height(self, side):
        self.set_side(side)
        
    def __str__(self):
        return "Square(side="+ str(self.width) + ")"
        
    
#     ###### TEST ######
    
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())
 
# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())
 
# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))
# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))