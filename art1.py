
import turtle
import random

class Art1:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def draw(self):
        num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = self.get_new_color()
        border_size = random.randint(1, 10)

        self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        reduction_ratio = 0.618

        turtle.penup()
        turtle.forward(size*(1 - reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1 - reduction_ratio)/2)
        turtle.right(90)

        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]
        size *= reduction_ratio

        self.draw_polygon(num_sides, size, orientation, location, color, border_size)

        turtle.update()
        turtle.done()
