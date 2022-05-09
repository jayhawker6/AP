import keyboard as kb
import turtle as ttl

ttl.screensize(250,200)
window = ttl.Screen() # Defining Screen

ball = ttl.Turtle() # Defining Ball
ball.speed(0)
ball.shape('circle')
ball.turtlesize(10)
ball.penup()

ceiling = ttl.Turtle(shape='square') # Defining ceiling
ceiling.speed(0)
ceiling.penup()
ceiling.setpos(0, 350)
ceiling.turtlesize(10, 50)

floor = ttl.Turtle(shape='square')
floor.speed(0)
floor.penup()
floor.setpos(0, -350)
floor.turtlesize(10, 50)
alive = True

inerta = 0
prevpressed = False
while alive:
    if inerta >= -10:
        inerta -= .2
    if kb.is_pressed(57):
        if prevpressed:
            pass
        else:
            inerta += 10
            prevpressed = True
    else:
        prevpressed = False
    if inerta > 10:
        inerta = 10
    if inerta < -10:
        inerta = -10
    ball.setpos(0, (ball.ycor() + inerta))
    if ball.distance(ceiling) < 200 or ball.distance(floor) < 200:
        alive = False

ttl.done()