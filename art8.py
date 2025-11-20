
import turtle
import random

class Art8:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for _ in range(200):
            t.penup()
            t.goto(0,0)
            t.pendown()
            t.color(random.randint(200,255), 0, random.randint(150,255))
            t.setheading(random.randint(0,360))
            t.forward(random.randint(50,350))

        turtle.update()
        turtle.done()
