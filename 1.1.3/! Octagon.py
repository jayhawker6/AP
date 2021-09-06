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

speed(0)
p.left(90)
p.hideturtle()

i = 0
while i != 8:
    p.forward(50)
    p.left(45)
    i += 1
#END OF PROGRAM#
wn.exitonclick()