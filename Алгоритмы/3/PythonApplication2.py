
import turtle           

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
gal = turtle.Turtle()
for x in range(10000):
    gal.forward(x)
    gal.left(200)
    gal.circle(x)
    gal.pencolor(colors[x%6])
    canvas = turtle.Screen()
    canvas.bgcolor("Ligthtgray")