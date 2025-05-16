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

def eskenarUcgenPrizma(a,h):
    return ((a**2)*math.sqrt(3))/2+3*a*h

def dikUcgenPrizma(b,c,a,h):
    return b*c+(a+b+c)*h

def silindir(r,h):
    return 2*math.pi*r*h + 2*math.pi*(r**2)

def eskenarDortgen(e,f):
    return e*f/2

def dikdortgenlerPrizmasi(a,b,c):
    return 2*(a*b + a*c + b*c)

def karePrizma(a,b):
    return 4*a*b + 2*a*a

print("Aşağıdaki seçeneklerden alanını hesaplamak istediğiniz geometrik şekli tuşlayınız....")
time.sleep(2)
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

secim = int(input("Seçiminiz nedir: "))

if secim == 1:
    kenr = int(input("Karenin bir kenarının uzunluğunu giriniz: "))
    alan = kare(kenr)
    print("Karenin alanı = {}".format(alan))
elif secim == 2:
    kkenr = int(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
    ukenr = int(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
    alan = dikdortgen(kkenr, ukenr)
    print("Dikdörtgenin alanı = {}".format(alan))
elif secim == 3:
    tbn = int(input("Üçgenin taban uzunluğunu giriniz: "))
    yuks = int(input("Üçgenin yüksekliğini giriniz: "))
    alan = ucgen(tbn, yuks)
    print("Üçgenin alanı = {}".format(alan))
elif secim == 4:
    atbn = int(input("Yamuğun alt taban uzunluğunu giriniz: "))
    utbn = int(input("Yamuğun üst taban uzunluğunu giriniz: "))
    yuks = int(input("Yamuğun yüksekliğini giriniz: "))
    alan = yamuk(atbn, utbn, yuks)
    print("Yamuğun alanı = {}".format(alan))
elif secim == 5:
    tbn = int(input("Paralelkenarın taban uzunluğunu giriniz: "))
    yuks = int(input("Paralelkenarın yüksekliğini giriniz: "))
    alan = paralelkenar(tbn, yuks)
    print("Paralelkenarın alanı = {}".format(alan))
elif secim == 6:
    knr = int(input("Küpün bir kenar uzunluğunu giriniz: "))
    alan = küp(knr)
    print("Küpün alanı = {}".format(alan))
elif secim == 7:
    tbn = int(input("Eşkenar üçgen prizmanın tabanının bir kenar uzunluğunu giriniz: "))
    yuks = int(input("Eşkenar üçgen prizmanın yüksekliğini giriniz: "))
    alan = eskenarUcgenPrizma(tbn, yuks)
    print("Eşkenar üçgen prizmanın alanı = {}".format(alan))
elif secim == 8:
    knr1 = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° bitişiğindeki 1. kenar uzunluğunu giriniz: "))
    knr2 = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° bitişiğindeki 2. kenar uzunluğunu giriniz: "))
    uknr = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° karşısındaki kenar uzunluğunu giriniz: "))
    yuks = int(input("Dik üçgen prizmanın yüksekliğini giriniz: "))
    alan = dikUcgenPrizma(knr1, knr2, uknr, yuks)
    print("Dik üçgen prizmanın alanı = {}".format(alan))
elif secim == 9:
    ycap = int(input("Silindirin taban yarıçapını giriniz: "))
    yuks = int(input("Silindirin yüksekliğini giriniz: "))
    alan = silindir(ycap, yuks)
    print("Silindirin alanı = {}".format(alan))
elif secim == 10:
    ksg1 = int(input("Eşkenar dörtgenin 1. köşegen uzunluğunu giriniz: "))
    ksg2 = int(input("Eşkenar dörtgenin 2. köşegen uzunluğunu giriniz: "))
    alan = eskenarDortgen(ksg1, ksg2)
    print("Eşkenar dörtgenin alanı = {}".format(alan))
elif secim == 11:
    en = int(input("Dikdörtgeneler prizmasının eninin uzunluğunu giriniz: "))
    boy = int(input("Dikdörtgeneler prizmasının boyunun uzunluğunu giriniz: "))
    yuks = int(input("Dikdörtgeneler prizmasının yüksekliğini giriniz: "))
    alan = dikdortgenlerPrizmasi(en, boy, yuks)
    print("Dikdörtgenler prizmasının alanı = {}".format(alan))
else:
    knr = int(input("Kare prizmanın, kare şeklinin kenar uzunluğunu giriniz: "))
    yuks = int(input("Kare prizmanın yüksekliğini giriniz: "))
    alan = karePrizma(knr, yuks)
    print("Kare prizmanın alanı = {}".format(alan))

# try-except bloklarına alınacak bazı yerlere geciktirmek için time.sleep() konulabilir, kod denenmedi denenmeli