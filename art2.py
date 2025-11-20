
import turtle
import random

class Art2:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for i in range(70):
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.width(random.randint(1,4))
            t.circle(i * 3)
            t.left(15)

        turtle.update()
        turtle.done()
