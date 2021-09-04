# EZ turtle commands by Andrew G #
import turtle
p = turtle.Turtle()
wn = turtle.Screen()
p.right(90)
def down(x):
    p.forward(x)
def up(x):
    p.backward(x)
def right(x):
    p.left(90)
    down(x)
    p.right(90)
def left(x):
    p.right(90)
    down(x)
    p.left(90)
def speed(x):
    p.speed(x)
def size(x):
    p.pensize(x)
# End of EZ turtle commands by Andrew G #

p.left(90)
speed(6)

i = 0
while i != 4:
    p.forward(100)
    p.right(90)
    i += 1
p.hideturtle()

#END OF CODE#
wn.exitonclick()