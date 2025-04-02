#Parametre alan üs alam işlemini yapan fonksiyon
# def ustel_sayi(sayi1,sayi2):
#     sayi = sayi1**sayi2
#     return sayi

# taban = input("Üs alma islemi için taban giriniz: ")
# üs = input("Üs alma islemi icin üs giriniz: ")
# print(ustel_sayi(int(taban),int(üs)))

#--------------------------------------------

#Parametre alan üs alma işlemini for döngüsü ile yapan fonksiyon
def ustel_sayi(sayi1,sayi2):
    carpim = 1
    for _ in range(sayi2):
        carpim  *= sayi1
    return carpim

taban = input("Üs alama işlemi için taban giriniz: ")
üs = input("Üs alma işlemi için üs giriniz: ")
print(ustel_sayi(int(taban),int(üs)))