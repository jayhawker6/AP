#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
ttl = trtl.Turtle()
ttl.pensize(40)
ttl.circle(20)
wn=trtl.Screen()
## Skeeter Sticks ##
legs = 8
length = 70
radAngle = 360 / legs
ttl.pensize(5)
loops = 0
offset = 0
while (offset < legs):
    ttl.goto(0,20)
    if offset < 4:
        ttl.setheading(radAngle*(offset*.45)-45)
    else:
        ttl.setheading(radAngle*(offset*.45)+84)
    ttl.forward(length)
    offset = offset + 1

## Eyes ##
ttl.penup()
ttl.pencolor("red")
ttl.goto(0,0)
ttl.setheading(0)
ttl.forward(15), ttl.pendown(), ttl.dot(), ttl.penup()
ttl.backward(30), ttl.pendown(), ttl.dot(), ttl.penup()

## End ##
ttl.hideturtle()
wn.mainloop()