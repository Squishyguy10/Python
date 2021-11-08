import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('white')
t = turtle.Turtle()
t.width(1)
t.speed(10)
side = 200
t.color('red')    

def draw_square():
    global side
    for i in range(4):
        t.fd(side)
        t.rt(90)    

def multiple_squares():
    x = -950
    global side
    for i in range(9):
        t.penup()
        t.goto(x, 0)
        t.pendown()
        draw_square()
        x += 200

def rotating_squares():
    t.speed(100)
    for i in range(72):
        draw_square()
        t.rt(5)

def rotating_growing_squares():
    t.speed(100)
    global side
    side = 25
    for i in range(72):
        draw_square()
        t.rt(5)
        side += 10

def random_squares():
    t.speed(100)
    global side
    for i in range(100):
        t.penup()
        x = randint(-950, 950)
        y = randint(-500, 500)
        side = randint(10, 100)
        t.goto(x, y)
        t.pendown()
        draw_square()

# draw_square()
# multiple_squares()
# rotating_squares()
# rotating_growing_squares()
random_squares()

turtle.done()