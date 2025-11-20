
import turtle
import random

class Art6:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for _ in range(120):
            t.penup()
            t.goto(0,0)
            t.pendown()
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.setheading(random.randint(0,360))
            t.forward(random.randint(100,300))

        turtle.update()
        turtle.done()
