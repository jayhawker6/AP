# EZ turtle commands by Andrew G #
import turtle
ttl = turtle.Turtle()
wn = turtle.Screen()

ttl.right(90)
def down(x):
    ttl.forward(x)
def up(x):
    ttl.backward(x)
def right(x):
    ttl.left(90)
    down(x)
    ttl.right(90)
def left(x):
    ttl.right(90)
    down(x)
    ttl.left(90)
def speed(x):
    ttl.speed(x)
def size(x):
    ttl.pensize(x)
# End of EZ turtle commands by Andrew G #
ttl.color('red', 'yellow')
ttl.begin_fill()
speed(0)
while True:
    ttl.forward(200)
    ttl.left(170)
    if abs(ttl.pos()) < 1:
        break
ttl.end_fill()
ttl.shape("classic")
# END OF PROGRAM #
wn.exitonclick()