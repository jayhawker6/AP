# EZ turtle commands by Andrew G #
import turtle
ttl = turtle.Turtle()
wn = turtle.setup(1920, 1080, 0, 0)
def speed(x):
    ttl.speed(x)
def size(x):
    ttl.pensize(x)
# End of EZ turtle commands by Andrew G #

def drawblock(x):
    ttl.setheading(0)
    ttl.color(x, x)
    ttl.begin_fill()
    ttl.forward(100)
    ttl.left(90)
    ttl.forward(50)
    ttl.left(90)
    ttl.forward(100)
    ttl.left(90)
    ttl.forward(50)
    ttl.end_fill()
    ttl.backward(50)


ttl.penup(), ttl.setpos(-50, -450), ttl.pendown()
speed(0)
i = 0
while True:
    if i % 2 == 1:
        drawblock("blue")
    else:
        drawblock("purple")
    i += 1
# END OF PROGRAM #
wn.exitonclick()