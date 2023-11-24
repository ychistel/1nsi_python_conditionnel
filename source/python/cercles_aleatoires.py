from random import randint
from turtle import *

def deplace(x,y):
    up()
    goto(x,y)
    down()
    
def carre(c):
    deplace(-c/2,-c/2)
    for i in range(4):
        forward(c)
        left(90)
    deplace(0,0)

dimension = 400
n = 100
i = 0
carre(dimension)

speed("fastest")
while i < n:
    x_centre = randint(-dimension//2+10 , dimension//2-10)
    y_centre = randint(-dimension//2+10 , dimension//2-10)
    if x_centre >= 0:
        r_x = dimension//2 - x_centre
    else:
        r_x = dimension//2 + x_centre
    if y_centre >= 0:
        r_y = dimension//2 - y_centre
    else:
        r_y = dimension//2 + y_centre
    if r_x < r_y:
        deplace(x_centre,y_centre-r_x)
        circle(r_x)
    else:
        deplace(x_centre,y_centre-r_y)
        circle(r_y)
    i = i + 1
    