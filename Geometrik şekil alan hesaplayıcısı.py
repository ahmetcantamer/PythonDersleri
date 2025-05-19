import time
import math

#Geometrik şekillerin alanlarının hesaplandığı kısım
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



#Geometrik şekillerin uzunluklarının alındığı ve yazdırıldığı kısım
def secim1():
    kenr = int(input("Karenin bir kenarının uzunluğunu giriniz: "))
    alan = kare(kenr)
    return print("Karenin alanı = {}".format(alan))
def secim2():
    kkenr = int(input("Dikdörtgenin kısa kenar uzunluğunu giriniz: "))
    ukenr = int(input("Dikdörtgenin uzun kenar uzunluğunu giriniz: "))
    alan = dikdortgen(kkenr, ukenr)
    return print("Dikdörtgenin alanı = {}".format(alan))
def secim3():
    tbn = int(input("Üçgenin taban uzunluğunu giriniz: "))
    yuks = int(input("Üçgenin yüksekliğini giriniz: "))
    alan = ucgen(tbn, yuks)
    return print("Üçgenin alanı = {}".format(alan))
def secim4():
    atbn = int(input("Yamuğun alt taban uzunluğunu giriniz: "))
    utbn = int(input("Yamuğun üst taban uzunluğunu giriniz: "))
    yuks = int(input("Yamuğun yüksekliğini giriniz: "))
    alan = yamuk(atbn, utbn, yuks)
    return print("Yamuğun alanı = {}".format(alan))
def secim5():
    tbn = int(input("Paralelkenarın taban uzunluğunu giriniz: "))
    yuks = int(input("Paralelkenarın yüksekliğini giriniz: "))
    alan = paralelkenar(tbn, yuks)
    return print("Paralelkenarın alanı = {}".format(alan))
def secim6():
    knr = int(input("Küpün bir kenar uzunluğunu giriniz: "))
    alan = küp(knr)
    return print("Küpün alanı = {}".format(alan))
def secim7():
    tbn = int(input("Eşkenar üçgen prizmanın tabanının bir kenar uzunluğunu giriniz: "))
    yuks = int(input("Eşkenar üçgen prizmanın yüksekliğini giriniz: "))
    alan = eskenarUcgenPrizma(tbn, yuks)
    return print("Eşkenar üçgen prizmanın alanı = {}".format(alan))
def secim8():
    knr1 = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° bitişiğindeki 1. kenar uzunluğunu giriniz: "))
    knr2 = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° bitişiğindeki 2. kenar uzunluğunu giriniz: "))
    uknr = int(input("Dik üçgen prizmanın, dik üçgen şeklinin, 90° karşısındaki kenar uzunluğunu giriniz: "))
    yuks = int(input("Dik üçgen prizmanın yüksekliğini giriniz: "))
    alan = dikUcgenPrizma(knr1, knr2, uknr, yuks)
    return print("Dik üçgen prizmanın alanı = {}".format(alan))
def secim9():
    ycap = int(input("Silindirin taban yarıçapını giriniz: "))
    yuks = int(input("Silindirin yüksekliğini giriniz: "))
    alan = silindir(ycap, yuks)
    return print("Silindirin alanı = {}".format(alan))
def secim10():
    ksg1 = int(input("Eşkenar dörtgenin 1. köşegen uzunluğunu giriniz: "))
    ksg2 = int(input("Eşkenar dörtgenin 2. köşegen uzunluğunu giriniz: "))
    alan = eskenarDortgen(ksg1, ksg2)
    return print("Eşkenar dörtgenin alanı = {}".format(alan))
def secim11():
    en = int(input("Dikdörtgeneler prizmasının eninin uzunluğunu giriniz: "))
    boy = int(input("Dikdörtgeneler prizmasının boyunun uzunluğunu giriniz: "))
    yuks = int(input("Dikdörtgeneler prizmasının yüksekliğini giriniz: "))
    alan = dikdortgenlerPrizmasi(en, boy, yuks)
    return print("Dikdörtgenler prizmasının alanı = {}".format(alan))
def secim12():
    knr = int(input("Kare prizmanın, kare şeklinin kenar uzunluğunu giriniz: "))
    yuks = int(input("Kare prizmanın yüksekliğini giriniz: "))
    alan = karePrizma(knr, yuks)
    return print("Kare prizmanın alanı = {}".format(alan))




print("Aşağıdaki seçeneklerden alanını hesaplamak istediğiniz geometrik şekli tuşlayınız....")
time.sleep(1)
print("1-) Kare,")
time.sleep(0.5)
print("2-) Dikdörtgen,")
time.sleep(0.5)
print("3-) Üçgen,")
time.sleep(0.5)
print("4-) Yamuk,")
time.sleep(0.5)
print("5-) Paralelkenar,")
time.sleep(0.5)
print("6-) Küp,")
time.sleep(0.5)
print("7-) Eşkenar Üçgen Prizma,")
time.sleep(0.5)
print("8-) Dik Üçgen Prizma,")
time.sleep(0.5)
print("9-) Silindir,")
time.sleep(0.5)
print("10-) Eşkenar Dörtgen,")
time.sleep(0.5)
print("11-) Dikdörtgenler Prizması,")
time.sleep(0.5)
print("12-) Kare Prizma")
time.sleep(0.5)



while 1:
    try:
        secim = int(input("Seçiminiz nedir: "))
        if secim > 12:
            print("Lütfen geçerli bir değer giriniz...")
        else:
            break
    except:
        print("Lütfen geçerli bir değer giriniz....")



if secim == 1:
    secim1()
elif secim == 2:
    secim2()
elif secim == 3:
    secim3()
elif secim == 4:
    secim4()
elif secim == 5:
    secim5()
elif secim == 6:
    secim6()
elif secim == 7:
    secim7()
elif secim == 8:
    secim8()
elif secim == 9:
    secim9()
elif secim == 10:
    secim10()
elif secim == 11:
    secim11()
else:
    secim12()
