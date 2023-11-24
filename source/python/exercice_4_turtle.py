from random import randint
from turtle import *

def direction_aleatoire():
    direction = randint(1,4)
    if direction == 1:
        right(0)
    elif direction == 2:
        left(90)
    elif direction == 3:
        left(180)
    else:
        right(90)
    return direction

    
def deplacer(x,y):
    up()
    goto(x,y)
    down()
    
def carre(c):
    deplacer(-c/2,-c/2)
    for i in range(4):
        forward(c)
        left(90)
    deplacer(0,0)


# Programme principal

dim = 200
carre(dim)
n=3000
x,y = position()
speed("fastest")
#while -dim//2 <= x <= dim//2 and -dim//2 <= y <= dim//2:
#while -100 < y < 100:
for i in range(n):
    direction_aleatoire()
    x,y = position()
    if x > 99.9:
        deplacer(-90,y)
    elif x < -99.9:
        deplacer(90,y)
    elif y > 99.9:
        deplacer(x,-90)
    elif y < -99.9:
        deplacer(x,90)
    forward(10)
    print(x,y)
    
