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


# END OF PROGRAM #
wn.mainloop()