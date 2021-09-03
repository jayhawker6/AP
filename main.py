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
ttl.hideturtle()
i = 1
def colorswitch():
    global i
    i += 1
    if i % 2 == 1:
        ttl.color("purple")
    else:
        ttl.color("magenta")
speed(0)
ttl.turtlesize(2)
ttl.penup()
down(150)
ttl.pencolor("green")
size(10)
ttl.pendown()
up(50)
ttl.right(45)
ttl.pencolor("lime")
ttl.backward(50)
ttl.forward(50)
ttl.left(45)
up(50)
ttl.left(45)
ttl.backward(50)
ttl.forward(50)
ttl.right(45)
up(75)
ttl.shape("circle")
ttl.turtlesize(1.5)
ttl.setheading(10)
colorswitch()
ttl.stamp()
ttl.penup()
for i in range(18):
    colorswitch()
    ttl.stamp()
    ttl.forward(20)
    ttl.left(20)
# END OF PROGRAM #
wn.exitonclick()