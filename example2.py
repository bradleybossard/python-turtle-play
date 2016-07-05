import turtle
import canvasvg

turtle.hideturtle()
turtle.speed()
for i in range(9):
    turtle.circle(50)
    turtle.right(40)

ts = turtle.getscreen()
canvas = ts.getcanvas()
canvasvg.saveall("output/example2.svg", canvas)
