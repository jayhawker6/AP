#   a114_nested_loops_4.py 
import turtle as turtle

ttl = turtle.Turtle()
ttl.penup()
ttl.goto(-200, 0)
ttl.pendown()


def peak(x,y):
    xend = x+200
    yend = y-0
    move_x = 1
    move_y = 1
    while (x < xend):

        while (y < 100):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = -1

        while (y > yend):
            x = x + move_x
            y = y + move_y
            ttl.goto(x,y)
        move_y = 1
peak(-200,0)
peak(0,0)

wn = turtle.Screen()
wn.mainloop()