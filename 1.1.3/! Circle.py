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


speed(5)
for i in range(18):
    p.forward(20)
    p.right(20)
#END OF PROGRAM#
wn.exitonclick()