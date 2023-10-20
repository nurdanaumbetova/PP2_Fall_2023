import math
class Point():
    def __init__(num,x1,y1,x2,y2):
        num.x1 = x1
        num.y1 = y1
        num.x2 = x2
        num.y2 = y2
        
    def show(num):
        print(f'x1 = {num.x1}, y1 = {num.y1}, x2 = {num.x2}, y2 = {num.y2}')
        
    def move(num):
        a1=int(input("update your x1: "))
        b1=int(input("update your y1: "))
        a2=int(input("update your x2: "))
        b2=int(input("update your y1: "))

        num.x1 = a1
        num.y1= b1
        num.x2 = a2
        num.y2 = b2
        
    def dist(num):
        a = num.x2 - num.x1
        b = num.y2 - num.y1
        a = abs(a)
        b = abs(b)
        
        num.distance = math.sqrt(a**2 + b**2)
        print(f'Distance is: {num.distance}')
        

point = Point(0, 0, 3, 4)
point.show()
point.move()
point.show()
point.dist()