from math import sqrt

def discriminant(a,b,c):
    return b**2-4*a*c

a = int(input("valeur du coefficient: "))
b = int(input("valeur du coefficient: "))
c = int(input("valeur du coefficient: "))

delta = discriminant(a,b,c)
if delta < 0:
    print("pas de racine")
elif delta > 0:
    print("2 racines")
else:
    print("1 racine")
    
if delta < 0:
    print("pas de racine")
elif delta > 0:
    x_1 = (-b
else:
    print("1 racine")