import math
from functools import reduce

'''
Q1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps. Write a program to compute the
distance current position after sequence of movements.
'''


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.originX = x
        self.originY = y

    def go_up(self,steps):
        self.y += steps

    def go_down(self,steps):
        self.y -= steps

    def go_left(self,steps):
        self.x += steps

    def go_right(self,steps):
        self.x -= steps

    def show_dist(self):
        _x = math.fabs(self.originX-self.x)
        _y = math.fabs(self.originY-self.y)
        _items = [_x, _y]
        _result = math.sqrt(reduce(lambda x, y: x ** 2 + y ** 2, _items))
        print("The distance covered from origin is: ", _result)


p1 = Robot(24,32)
p1.go_up(5)
p1.go_down(3)
p1.go_left(3)
p1.go_right(2)
p1.show_dist()

