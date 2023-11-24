from random import randint
from turtle import *

def marche_aleatoire():
    direction = randint(1,6)
    forward(20)
    if direction == 1:
        right(0)
    elif direction == 2:
        left(60)
    elif direction == 3:
        left(120)
    elif direction == 4:
        left(180)
    elif direction == 5:
        left(240)
    else:
        right(60)

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

dim = 400
carre(dim)
x,y = position()
print(x,y)
while -dim//2 <= x <= dim//2 and -dim//2 <= y <= dim//2:
    marche_aleatoire()
    x,y = position()
    
