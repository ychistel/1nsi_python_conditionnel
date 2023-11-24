def syracuse(n):
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        print(n, end='-')
        
def temps_de_vol(n):
    tps = 0
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        tps += 1
    return tps

def vol_en_altitude(n):
    vol = n
    tps = 0
    if n % 2 == 0:
        return 0
    else:
        n = 3*n + 1
    while n >= vol:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        tps += 1
    return tps

def altitude_max(n):
    alt = n
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        if alt < n:
            alt = n
    return alt

# programme principal

n = 129
syracuse(n)
print()
print("Temps de vol:",temps_de_vol(n))
print("Temps de vol en altitude:",vol_en_altitude(n))
print("Alitude max:",altitude_max(n))