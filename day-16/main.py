# importing 'Turtle class' and 'Screen class' from 'turtle module'
# turtle package is preloaded in every copy of python
# from turtle import Turtle, Screen
#
# # constructing new object:
# timmy = Turtle()  # Turtle is a class
# print(type(timmy))
# timmy.shape("turtle")  # change the shape of the turtle
# timmy.color("cyan", "DarkRed")
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
#
# my_screen = Screen()  # Screen() is a class
# print(my_screen.canvwidth)  # canvwidth is an attribute from Screen class (literally a screen)
# my_screen.exitonclick()  # allow us to exit from the screen when click on it

# to install another package
# File: Settings: 'name of the project': Python Interpreter: add: 'search for the package you want to install'


#################################################################################################
#################################################################################################
from prettytable import PrettyTable

table = PrettyTable()

# .add_column method: field name, then a list of thw rows above
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "c"   # setting an attribute type
print(table)