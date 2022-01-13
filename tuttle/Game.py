import turtle as trtl
import random as rand
import time


#-------------Variables---------
shape = 'square'
shape_x_sz = 8
shape_y_sz = 8


sequence_list = []
working_list = []
#-------------Turtles


#Makes the screen turtle
screen = trtl.Screen()
screen.tracer(False)
#Makes the turtles for the game
shape_top_left = trtl.Turtle()
shape_top_right = trtl.Turtle()
shape_bottom_left = trtl.Turtle()
shape_bottom_right = trtl.Turtle()

shape_top_left.penup()
shape_top_right.penup()
shape_bottom_left.penup()
shape_bottom_right.penup()


shape_top_left.shape(shape)
shape_top_right.shape(shape)
shape_bottom_left.shape(shape)
shape_bottom_right.shape(shape)

shape_top_left.shapesize(shape_x_sz,shape_y_sz)
shape_top_right.shapesize(shape_x_sz,shape_y_sz)
shape_bottom_left.shapesize(shape_x_sz,shape_y_sz)
shape_bottom_right.shapesize(shape_x_sz,shape_y_sz)

#sets color theme for the shape
shape_top_left.color('#c785ec')
shape_top_right.color('#a86add')
shape_bottom_left.color('#8549a7')
shape_bottom_right.color('#634087')

screen.bgcolor('#deb7ff')
#Move the turtles

shape_top_left.goto(-80,80)
shape_top_right.goto(80,80)
shape_bottom_left.goto(-80,-80)
shape_bottom_right.goto(80,-80)
screen.tracer(True)

def follow_sequence():
    
    if len(sequence_list) > 0:
        for num in sequence_list:
            working_list.append(num)
        for num in working_list:
            
    else:
        sequence()

    




def sequence():
    global rand_num
    rand_num = rand.randint(1,4)
    sequence_list.append(rand_num)
    print('lsit' + str(sequence_list))





def click(x,y):
    time.sleep(.5)
    shape_top_left.color('white')
    shape_top_right.color('white')
    shape_bottom_left.color('white')
    shape_bottom_right.color('white')
    time.sleep(.5)
    shape_top_left.color('#c785ec')
    shape_top_right.color('#a86add')
    shape_bottom_left.color('#8549a7')
    shape_bottom_right.color('#634087')






screen.onclick(click)


screen.mainloop()