import PythonClass
import turtle

tur = turtle.Turtle()
scr = turtle.Screen()

def move_forward():
    tur.forward(10)


def move_backward():
    tur.backward(10)


scr.listen()
scr.onkey(move_forward(), "f")
scr.exitonclick()

amz = PythonClass.Amsikkakuzhi
amz.church()