def karesini_al(x):
    return x**2   #kare alma işlemi x*x de yapılabilir

#---------------------------------------------------

# kare_liste = []
# sayilar = list(range(1,6))
# for kareleri in sayilar:
#     kare_liste.append(karesini_al(kareleri))
# print(kare_liste)

#----------------------------------------------

# sayilar = list(range(1,6))
# kare_liste = list(range(len(sayilar)))
# for kareleri in range(len(sayilar)):
#     kare_liste[kareleri] = karesini_al(sayilar[kareleri])
# print(kare_liste)

#-------------------------------------------------

# sayilar = [*range(1,6)]
# list(map(karesini_al, sayilar))   #map kullanarak üstteki ifadelerin aynısını yaptık
# print(list(map(karesini_al, sayilar)))

#------------------------------------------

# def cift_sayilar_filtrele(x):
#     #if x%2 == 0:
#         #return x
#     return x if x%2 == 0 else None    #filtre kullanmadan
# print(cift_sayilar_filtrele(10))

#-------------------------------------------

# def cift_sayilar_filtrele(x):
# #     #if x%2 == 0:
# #         #return x
#     return x if x%2 == 0 else None
# sayilar = [*range(1,6)]
# filter(cift_sayilar_filtrele,sayilar)       #filter ifadesi kullanılarak yapılan ifade
# print([*filter(cift_sayilar_filtrele,sayilar)])

#---------------------------------------------------

sayilar = list(range(1,6))
map(lambda sayi:sayi**2,sayilar)        #lambda kullanarak işlemi tekrar yaptık
print(list(map(lambda sayi:sayi**2,sayilar)))


















