"""
#Dunder(Double Under Score)
class Ucus():
    havayolu = "THY"
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod1 = kod
        self.kalkis1 = kalkis
        self.varis1 = varis
        self.sure1 = sure
        self.kapasite1 = kapasite
        self.yolcu1 = yolcu
    
    def __repr__(self):
        return "{} sefer sayili ucus, sistemde olusturulmustur".format(self.kod1)
    
    def anos_yap(self):
        return "{} sefer sayili {}---{} ucusumuz {} dakika sürecektir.".format(
            self.kod1,
            self.kalkis1,
            self.varis1,
            self.sure1)
    
    def bos_koltuk_sayisi(self):
        return self.kapasite1 - self.yolcu1
    
    def bilet_satis(self, bilet_adet = 1):
        if self.yolcu1 + bilet_adet <= self.kapasite1:
            self.yolcu1 += bilet_adet
            self.bos_koltuk_sayisi()
            print("{} adet bilet satilmistir, kalan koltuk sayisi {}".format(bilet_adet, self.bos_koltuk_sayisi()))
        else:
            print("Islem gerceklestirilemedi")

    def bilet_iptal(self, bilet_adedi = 1):
        if self.yolcu1 >= bilet_adedi:
            self.yolcu1 -= bilet_adedi
            print("{} adet bilet iptal edilmistir, kalan koltuk sayisi {}".format(bilet_adedi, self.bos_koltuk_sayisi()))
        else:
            print("Islem gerceklestirilemedi")

ucus1 = Ucus('TK112', 'DEN', 'IST', 60, 130, 110)
print(ucus1.__dir__())
print(ucus1) #Üstte __repr__ yazmasaydık gerip yazılar gözükecekti
#ama repr yazdığımız için reppr'ın içine ne yazdırdıysak o gözükecek
"""

class Seyehat():
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis
        
    def anons(self):
        return "{}--{} seyehatine hosgeldiniz".format(self.kalkis, self.varis)
    
class Otobus(Seyehat):
    def __init__(self, mola_duraklari):
        Seyehat.__init__(self, 'IST', 'ANK')
        self.mola_duraklari = mola_duraklari
        
    
seyehat = Seyehat("ANT", "BOD")
print(seyehat.kalkis)
oto1 = Otobus(['FET','ALAN'])
print(oto1.mola_duraklari)
print(oto1.kalkis)
    