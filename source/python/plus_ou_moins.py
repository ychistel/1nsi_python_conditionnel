from random import randint

n = randint (1,100)
rep = False

while rep == False:
    prop = int(input("proposer un nombre entre 1 et 100: "))
    if prop == n:
        print("gagné")
        rep = True
    else:
        if prop < n:
            print("plus grand")
        else:
            print("moins grand")

