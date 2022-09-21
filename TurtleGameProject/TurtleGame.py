import turtle

scr = turtle.Screen()

scr.setup(height=600,width=700)
user_bet = scr.textinput(title="Make your bet", prompt="Which turtle will win?\nEnter color:")

tur_red = turtle.Turtle(shape="turtle")
tur_red.color("Red")
tur_red.penup()
tur_red.goto(x=-180, y=-150)

tur_orange = turtle.Turtle(shape="turtle")
tur_orange.color("orange")
tur_orange.penup()
tur_orange.goto(x=-180, y=-100)

tur_yellow = turtle.Turtle(shape="turtle")
tur_yellow.color("yellow")
tur_yellow.penup()
tur_yellow.goto(x=-180, y=-50)

scr.exitonclick()

