#from Tkinter import *
#from turtle import *
import turtle
import canvasvg

def thing():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)

turtle.speed()
thing()
ts = turtle.getscreen()
canvas = ts.getcanvas()
canvasvg.saveall("example1.svg", canvas)
#ts.getcanvas().postscript(file="example1.svg")
