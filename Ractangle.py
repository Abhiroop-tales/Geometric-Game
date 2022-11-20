from random import randint
import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x)*(self.point2.y - self.point1.y)


class GuiRectangle(Rectangle):
    def draw(self, myTurtle):
        # Go to Certain coordinate
        myTurtle.penup()
        myTurtle.goto(self.point1.x,self.point1.y)

        myTurtle.pendown()
        myTurtle.forward(self.point2.x - self.point1.x)
        myTurtle.left(90)
        myTurtle.forward(self.point2.y - self.point1.y)
        myTurtle.left(90)
        myTurtle.forward(self.point2.x - self.point1.x)
        myTurtle.left(90)
        myTurtle.forward(self.point2.y - self.point1.y)
        

class GuiPoint(Point):
    def draw(self, myTurtle):
        myTurtle.penup()
        myTurtle.goto(self.x,self.y)
        myTurtle.pendown()
        myTurtle.dot(5,'red')

        

# Create Random Rectangle
rect = GuiRectangle(Point(randint(0,9), randint(0,9)),Point(randint(10,19), randint(10,19))) 

print("Rectangle Corrdinates of diagonal: ", rect.point1.x ,", ",rect.point1.y, " and ", rect.point2.x,",",rect.point2.y)

# Get points and area from the user
user_point = GuiPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess area : "))

print("Your point guess is: ", user_point.falls_in_rectangle(rect))
print("Your area was off by: ", rect.area()-user_area)
canavas = turtle.Turtle()
rect.draw(canavas)
user_point.draw(canavas)
turtle.done()