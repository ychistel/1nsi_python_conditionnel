from turtle import *
from math import sqrt

c = 240

for i in range(8):
    for i in range(4):
        forward(c)
        left(90)
    forward(c/2)
    left(45)
    c = c/sqrt(2)

hideturtle()

    
