import random
from turtle import Turtle, color
timy=Turtle()


def abc(sides):
    angel=360/sides
    for _ in range(sides):
        timy.forward(100)
        timy.right(angel)
color=["medium blue","light sea green	","green","olive","peru","firebrick","orange red","deep pink","purple","indigo"]        

for shape in range(3,11):
    timy.color(random.choice(color))
    abc(shape)

screen=t.Screen()
screen.exitonclick()
