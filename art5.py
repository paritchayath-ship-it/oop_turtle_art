
import turtle
import random

class Art5:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for _ in range(100):
            t.penup()
            t.goto(random.randint(-350,350), random.randint(-250,250))
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.pendown()
            t.begin_fill()
            t.circle(random.randint(10,40))
            t.end_fill()

        turtle.update()
        turtle.done()
