#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
ttl = trtl.Turtle()
ttl.pensize(40)
ttl.circle(20)
wn=trtl.Screen()
legs = 8
length = 70
radAngle = 380 / legs
ttl.pensize(5)
loops = 0
while (n < legs):
    ttl.goto(0,0)
    ttl.setheading(radAngle*n)
    ttl.forward(length)
    n = n + 1
ttl.hideturtle()
wn.mainloop()