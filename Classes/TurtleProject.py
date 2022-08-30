# import turtle
#
# my_turtle = turtle.Turtle
#
# cv = my_turtle
# print(cv)
# my_turtle.shape("triangle")
# my_turtle.color("red")
#
# my_screen = turtle.Screen()
#
# my_screen.screensize()
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Name", ["Bensly", "Angel", "Athara"])
table.add_column("Age", [30, 28, 1])
table.add_column('Job', ['QA', 'Prod', 'Baby'])

print(table)

print(type(table))
print((type(prettytable)))

