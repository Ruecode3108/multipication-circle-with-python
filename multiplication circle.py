import turtle
import math

r = turtle.Turtle()
r.speed(0)
r.color('gold')

n = 50  
m=2
for i in range(n):
    angle_i = 2 * math.pi * i / n
    x_i = 100 * math.cos(angle_i)
    y_i = 100 * math.sin(angle_i)
    j = (i * m) % n
    angle_j = 2 * math.pi * j / n
    x_j = 100 * math.cos(angle_j)
    y_j = 100 * math.sin(angle_j)
    r.penup()
    r.goto(x_i, y_i)
    r.pendown()
    r.goto(x_j, y_j)

turtle.done()

