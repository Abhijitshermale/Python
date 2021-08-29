import random
from turtle import Turtle

timy=Turtle()

color=["medium blue","light sea green","green","olive","peru","firebrick","orange red","deep pink","purple","indigo"]        
dir=[0,90,180,270]
# timy.speed("Fastest")
timy.pensize(15)


for _ in range(200):
    timy.color(random.choice(color))
    timy.forward(30)
    timy.setheading(random.choice(dir))
