import turtle as turtle_module
from turtle import Screen
import random
# import colorgram as cg
# colors = cg.extract('image.jpg',25)
# lst = []
# for i in range(25):
#     color = colors[i]
#     rgb = color.rgb
#     red = rgb.r
#     green = rgb.g
#     blue = rgb.b
#     tup = (red,green,blue)
#     lst.append(tup)
#     # print(tup)
# print(lst)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(199, 175, 117), (125, 36, 24), (167, 106, 56), (186, 159, 52), (6, 57, 83), (108, 68, 85),
               (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35), (76, 40, 48), (9, 68, 47), (90, 141, 52),
               (182, 96, 79), (131, 38, 41), (141, 171, 156), (210, 200, 149), (179, 201, 186), (173, 153, 159),
               (212, 183, 176), (151, 114, 119)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()
