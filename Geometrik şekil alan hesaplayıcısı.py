import time
import math

def kare(a):
    return a*a

def dikdortgen(a,b):
    return a*b

def ucgen(a,h):
    return (a*h)/2

def yamuk(a,c,h):
    return (a+c)*h/2

def paralelkenar(a,h):
    return a*h

def küp(a):
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

secim = input()

if secim == "1":
    kenr = int(input("Karenin bir kenarının uzunluğunu giriniz: "))
    alan = kare(kenr)
    print("Karenin alanı = ".format(alan))
elif secim == "2":
    kkenr = int(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
    ukenr = int(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
    alan = dikdortgen(kkenr, ukenr)
    print("Dikdörtgenin alanı = ".format(alan))
elif secim == "3":
    tbn = int(input("Üçgenin taban uzunluğunu giriniz: "))
    yuks = int(input("Üçgenin yüksekliğini giriniz: "))
    alan = ucgen(tbn, yuks)
    print("Üçgenin alanı = ".format(alan))
elif secim == "4":
    atbn = int(input("Yamuğun alt taban uzunluğunu giriniz: "))
    utbn = int(input("Yamuğun üst taban uzunluğunu giriniz: "))
    yuks = int(input("Yamuğun yüksekliğini giriniz: "))
    alan = yamuk(atbn, utbn, yuks)
    print("Yamuğun alanı = ".format(alan))
elif secim == "5":
    tbn = int(input("Paralelkenarın taban uzunluğunu giriniz: "))
    yuks = int(input("Paralelkenarın yüksekliğini giriniz: "))
    alan = paralelkenar(tbn, yuks)
    print("Paralelkenarın alanı = ".format(alan))
elif secim == "6":
    knr = int(input("Küpün bir kenar uzunluğunu giriniz: "))
    alan = küp(knr)
    print("Küpün alanı = ".format(alan))
