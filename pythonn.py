import math
import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("red")
t.speed(0)
t.width(2)

turtle.tracer(0)  # deixa MUITO mais rápido

def heart_x(k):
    return 16 * math.sin(k)**3

def heart_y(k):
    return 13 * math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

t.penup()

first = True
for i in range(0, 628):
    k = i / 10* math.pi
    x = heart_x(k) * 15
    y = heart_y(k) * 15

    if first:
        t.goto(x, y)
        t.pendown()
        first = False
    else:
        t.goto(x, y)

turtle.update()

# Mensagem
t.penup()
t.goto(0, -200)
t.color("white")
t.write("LOVE", align="center", font=("Arial", 24, "bold"))

turtle.done()
