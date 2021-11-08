import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('white')

t = turtle.Turtle()
t.width(2)
t.speed(8)
t.color('red')
t.penup()
t.goto(-955, 500)
t.pendown()
side_height = 990
side_width = 1900

for i in range(2):
    t.fd(side_width)
    t.rt(90)
    t.fd(side_height)
    t.rt(90)
    
turtle.done()