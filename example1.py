#from Tkinter import *
#from turtle import *
import turtle

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

ts = turtle.getscreen()
ts.getcanvas().postscript(file="example1.svg")
