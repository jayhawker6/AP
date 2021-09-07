#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
ttl = trtl.Turtle()
ttl.pensize(40)
ttl.circle(20)
w = 6
y = 70
z = 380 / w
ttl.pensize(5)
n = 0
while (n < w):
    ttl.goto(0,0)
    ttl.setheading(z*n)
    ttl.forward(y)
    n = n + 1
ttl.hideturtle()
wn = trtl.Screen()
wn.mainloop()