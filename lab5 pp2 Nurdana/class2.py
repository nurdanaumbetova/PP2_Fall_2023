class Shape:
    def __init__(a, area):
        a.area = area
        
    def printArea(a):
        print(a.area)

class Square(Shape):
    def __init__(a, length):
        area = length * length
        super().__init__(area)
        a.length = length
        

    def printArea(a):
        print(f"The area is {a.area}")


a = Square(int(input()))  
a.printArea()