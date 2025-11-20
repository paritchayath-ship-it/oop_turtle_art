
import turtle
import random

class Art3:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def star(self, size):
        t = turtle.Turtle()
        t.hideturtle()
        t.color(random.randint(100,255), random.randint(100,255), random.randint(100,255))
        t.penup()
        t.goto(random.randint(-300,300), random.randint(-250,250))
        t.pendown()

        for _ in range(5):
            t.forward(size)
            t.right(144)

    def draw(self):
        for _ in range(50):
            self.star(random.randint(20,80))

        turtle.update()
        turtle.done()
