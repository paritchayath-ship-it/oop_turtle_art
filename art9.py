
import turtle
import random

class Art9:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for i in range(100):
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.circle(i * 2)
            t.left(10)

        turtle.update()
        turtle.done()
