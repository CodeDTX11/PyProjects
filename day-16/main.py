from turtle import Turtle, Screen

from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("teal")
# timmy.forward(100)
# my_screen = Screen()
# # print(my_screen)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Poke Name", ["pik", "squrt", "charz"])
table.add_column("typo", ["elec", "wet", "lit"])

table.align = 'l'

print(table)