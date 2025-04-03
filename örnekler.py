#Parametre alan üs alam işlemini yapan fonksiyon
# def ustel_sayi(sayi1,sayi2):
#     sayi = sayi1**sayi2
#     return sayi

# taban = input("Üs alma islemi için taban giriniz: ")
# üs = input("Üs alma islemi icin üs giriniz: ")
# print(ustel_sayi(int(taban),int(üs)))

#--------------------------------------------

#Parametre alan üs alma işlemini for döngüsü ile yapan fonksiyon
# def ustel_sayi(sayi1,sayi2):
#     carpim = 1
#     for _ in range(sayi2):
#         carpim  *= sayi1
#     return carpim

# taban = input("Üs alama işlemi için taban giriniz: ")
# üs = input("Üs alma işlemi için üs giriniz: ")
# print(ustel_sayi(int(taban),int(üs)))

#-----------------------------------------------

#Bir parametre alan ve listedeki en büyük iki sayıyı döndüren fonksiyon
# def listedeki_en_buyuk_iki_sayi(liste):
#     liste.sort()
#     sayi1 = liste.pop()
#     sayi2 = liste.pop()
#     return sayi1,sayi2

# liste = []
# for i in range(5):
#     liste.append(int(input("{}. sayiyi giriniz: ".format(i+1))))

# gelen_sayi1,gelen_sayi2 = listedeki_en_buyuk_iki_sayi(liste)
# print("Listedeki en büyük iki sayi = {}, {}".format(gelen_sayi1,gelen_sayi2))

#-------------------------------------------------------

#Bir parametre alan ve listedeki stringleri döndüren fonksiyon
# def str_filtrele(liste):
#     yenilist = []
#     for i in range(len(liste)):
#         if liste[i].isdigit():
#             pass
#         else:
#             yenilist.append(liste[i])
#     return yenilist
    

# liste = []
# for i in range(7):
#     eklenecek = input("Listeye eklenecek {}. elemani giriniz: ".format(i+1))
#     liste.append(eklenecek)
    
# print(str_filtrele(liste))

#---------------------------------------------------

#Bir parametre alan ve listedeki stringleri filter ve lambda kullanarak döndüren fonksiyon

def str_filtrele2(liste):
    return [*filter(lambda x: x if type(x) == str else None, liste)]

print(str_filtrele2([1,2,3,5,"abc",'a']))





