# def tam_sayiya_cevir():
#     girdi = input("Bir ondalik sayi giriniz: ")
#     print("Yuvarlama isleminin sonucu = {}".format(round(float(girdi))))
    
# tam_sayiya_cevir()

#--------------------------------------------

#Try-except ile kullanımı;
# def tam_sayiya_cevir():
#     girdi = input("Bir ondalik sayi giriniz: ")
    
#     try:
#         girdi = float(girdi)
#         print("Yuvarlama isleminin sonucu: {}".format(round(girdi)))
#     except:
#         print("{} girdisi ondalik tipe cevrilemiyor, lütfen gecerli bir deger giriniz.".format(girdi))

# tam_sayiya_cevir()

#---------------------------------------------

#Try-except ve finally ile kullanımı;
# def tam_sayiya_cevir():
#     girdi = input("Bir ondalik sayi giriniz: ")
#     durum = ""
#     try:
#         girdi = float(girdi)
#         print("Yuvarlama isleminin sonucu: {}".format(girdi))
#         durum = "Basarili"
#     except:
#         print("{} girdisi ondalik tipe cevrilemiyor, lütfen gecerli bir deger giriniz.".format(girdi))
#         durum = "Basarisiz"
#     finally:
#         print("Tam sayiya cevirme islemi {} olustur".format(durum))
        
# tam_sayiya_cevir()

#----------------------------------------------

def tam_sayiya_cevir_dongu():
    while True:
        girdi = input("Bir ondalik sayi giriniz: ")
        
        try:
            girdi = float(girdi)
            print("Yuvarlama isleminin sonucu: {}".format(round(girdi)))
            break
        except:
            print("Hatali giris yaptiniz, lütfen tekrar deneyiniz.")
            
            
tam_sayiya_cevir_dongu()
    
    
    
    
    
    
    
    
    
    
    