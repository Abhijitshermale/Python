# import colorgram
#
# rgb_colors=[]
# colors= colorgram.extract('image.jpg',30)
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import random
import turtle as t

t.colormode(255)
timy=t.Turtle()
timy.speed("fastest")
timy.penup()
timy.hideturtle()
color_list=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

timy.setheading(225)
timy.forward(300)
timy.setheading(0)
numbers_of_dot=100


for dot_count in range(1,numbers_of_dot+1):
    timy.dot(20,random.choice(color_list))
    timy.forward(50)

    if dot_count % 10==0:
        timy.setheading(90)
        timy.forward(50)
        timy.setheading(180)
        timy.forward(500)
        timy.setheading(0)

screen=t.Screen()
screen.exitonclick()

