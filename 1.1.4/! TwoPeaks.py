#   a114_nested_loops_4.py 
import turtle
import random

ttl = turtle.Turtle()
ttl.penup()
ttl.goto(-200, 0)
ttl.pendown()


def peak(x,y):
    xend = x+200
    yend = y-0
    move_x = 1
    move_y = 1
    while (x < xend):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = -1

        while (y > yend):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = 1
def peakTwo(x,y):
    xend = x-200
    yend = y-0
    move_x = -1
    move_y = -1
    while (x > xend):

        while (y > -100):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = 1

        while (y < yend):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = -1
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
def colorchange():
    global colors
    color = random.choice(colors)
    ttl.pencolor(color), ttl.color(color)
ttl.pensize(5)
ttl.hideturtle()
while True:
    colorchange()
    peak(-200,0)
    peak(0,0)
    peakTwo(200,0)
    peakTwo(0,0)