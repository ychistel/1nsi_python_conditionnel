from turtle import *
from math import sqrt

l = 20
n = 10

left(45)
for _ in range(4):
    for _ in range(n):
        forward(l)
        right(90)
        forward(l)
        left(90)
    right(90)    
