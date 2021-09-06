import turtle
wn = turtle.Screen()
ttl = turtle.Turtle()

#CODE START#
ln = 501
ttl.speed(0)
while ln != 500:
    for i in range(500):
        ttl.circle(i)
    ttl.forward(5)
    ln += 1
wn.exitonclick()