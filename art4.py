
import turtle
import random

class Art4:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor("black")
        turtle.tracer(0)
        turtle.colormode(255)

    def draw(self):
        t = turtle.Turtle()
        t.hideturtle()

        for i in range(50):
            t.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            t.penup()
            t.goto(0,0)
            t.pendown()

            t.setheading(i * 10)
            for _ in range(4):
                t.forward(120)
                t.right(90)

        turtle.update()
        turtle.done()
