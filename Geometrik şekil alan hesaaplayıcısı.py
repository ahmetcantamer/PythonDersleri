import time
import math

def kare():
    return a*a

def dikdortgen():
    return a*b

def ucgen():
    pass

def yamuk():
    return (a+c)*h/2

def paralelkenar():
    return a*h

def küp():
    return 6*(a**2)

def eskenarUcgenPrizma():
    return ((a**2)*math.sqrt(3))/2+3*a*h

def dikUcgenPrizma():
    return b*c+(a+b+c)*h

def silindir():
    return 2*math.pi*r*h + 2*math.pi*(r**2)

def eskenarDortgen():
    return e*f/2

def dikdortgenlerPrizmasi():
    return 2*(a*b + a*c + b*c)

def karePrizma():
    return 4*a*b + 2*a*a

print("Aşağıdaki seçeneklerden alanını hesaplamak istediğiniz geometrik şekli tuşlayınız....")
time.sleep(1)
print("""
        1-) Kare,
        2-) Dikdörtgen,
        3-) Üçgen,
        4-) Yamuk,
        5-) Paralelkenar,
        6-) Küp,
        7-) Eşkenar Üçgen Prizma,
        8-) Dik Üçgen Prizma,
        9-) Silindir,
        10-) Eşkenar Dörtgen,
        11-) Dikdörtgenler Prizması,
        12-) Kare Prizma
"""  )