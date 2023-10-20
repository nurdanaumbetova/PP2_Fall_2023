class Shape:
    def __init__(a, area):
        a.area = area
        
    def printArea(a):
        print(a.area)

class Square(Shape):
    def __init__(a, length, width):
        area = length * width
        super().__init__(area)
        a.length = length
        a.width = width

    def printArea(a):
        print(f"The area is {a.area}")


a = Square(5,8)  
a.printArea()