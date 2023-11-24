from turtle import *

largeur = 450
hauteur = 200
x,y = 80,0
dx,dy = 1,1
n = 100000
couleur = ['red','blue','green','yellow','orange','purple','brown']

setworldcoordinates(0,0,largeur,hauteur)

for i in range(2):
    forward(largeur)
    left(90)
    forward(hauteur)
    left(90)

up()
goto(x,y)
down()

for i in range(n):
    if x >= largeur:
        dx = -1
        color(couleur[i%7])
    if x <= 0:
        dx = 1
        color(couleur[i%7])
    if y >= hauteur:
        dy = -1
        color(couleur[i%7])
    if y <= 0:
        dy = 1
        color(couleur[i%7])
    x = x + dx
    y = y + dy
    goto(x,y)
    
        
    
        

