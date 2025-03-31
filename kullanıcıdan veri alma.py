# girdi = input("Bir sayi girin: ")
# print(type(girdi))      #string tipinde veri döndürür

#------------------------------------

# def uygulama():
#     girdi = input("Bir sayi giriniz: ")
#     islem = input("Girdiginiz sayi cift mi tek mi: ")
#     if islem == 'cift':
#         if int(girdi)%2 == 0:
#             return 'Evet cift sayidir.'
#         else:
#             return 'Hayir cift sayi degildir.'
#     elif islem == 'tek':
#         if int(girdi)%2 == 1:
#             return 'Evet tek sayidir.'
#         else:
#             return 'Hayir tek sayi degildir.'
        
# print(uygulama())

#----------------------------------------

# def sayi_girdisi_kontrol():
#     girdi = input("Bir sayi giriniz: ")
    
#     if girdi.isdigit():
#         print("Sayi tipi deger girdiniz.")
#     else:
#         print("Bu bir sayi tipi degisken degildir.")

# sayi_girdisi_kontrol()

#-------------------------------------

# def sayi_girdisi_kontrol():
#     girdi = input('Bir sayi giriniz: ')
#     if girdi.isdigit():
#         print("Sayi tipi deger girdiniz.")
#     else:
#         while not girdi.isdigit():
#             print("Girilen deger sayi tipinde degildir.")
#             girdi = input('Bir sayi giriniz: ')
#         print("Tebrikler sayi degeri girebildiniz.")

# sayi_girdisi_kontrol()

#----------------------------------------

#üsteki kodun daha sade hali(if-else olmadan)        
# def sayi_girdisi_kontrol():
#     girdi = input('Bir sayi giriniz: ')
#     while not girdi.isdigit():
#         print("Girilen deger sayi tipinde degildir.")
#         girdi = input('Bir sayi giriniz: ')
            
#     print("Tebrikler sayi degeri girdiniz.")

# sayi_girdisi_kontrol()  
    
#-------------------------------------------------           
 
#E-posta kontrol edici kod
"""Aşağıdaki kodda, eğer girilen ifade içinde . ve @ işaretleri varsa
e-postamız geçerli bir e-posta demektir ama bu ifadeler yer almıyorsa
bu geçerli bir e-posta değildir."""
def eposta_kontrol():
    girdi = input("Bir E-posta adresi giriniz: ")
    while not (('.' in girdi) and ('@' in girdi)):
        print("Bu bir E-posta adresi degildir, lutfen gecerli bir E-posta adresi giriniz")
        girdi = input("Bir E-posta adresi giriniz: ")
    print("Tebrikler, girilen E-posta adresi geçerli bir E-postadir.")

eposta_kontrol()