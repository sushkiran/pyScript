import math
from functools import reduce

'''
Q1. A Robot moves in a Plane starting from the origin point (0,0). The robot can move
toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given
following: UP 5, DOWN 3, LEFT 3, RIGHT 2
The numbers after directions are steps. Write a program to compute the
distance current position after sequence of movements.
'''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y):
        self.origin = Point(x, y)
        self.move = Point(x, y)

    def go(self, up, down, left, right):
        self.move.y += up
        self.move.y -= down
        self.move.x += left
        self.move.x -= right

    def show_dist(self):
        diff_array = [(self.origin.x - self.move.x), (self.origin.y - self.move.y)]
        dist = math.sqrt(reduce(lambda x, y: x ** 2 + y ** 2, diff_array))
        print("The distance covered from origin is: ", dist)


p1 = Robot(0, 0)
p1.go(up=5, down=3, left=3, right=2)
p1.show_dist()

