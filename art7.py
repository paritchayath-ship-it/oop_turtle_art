
import turtle
import random

class Art7:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for i in range(80):
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.circle(100)
            t.left(360/80)

        turtle.update()
        turtle.done()
