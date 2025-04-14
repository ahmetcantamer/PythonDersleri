class Ucus():
    havayolu = "THY"
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod1 = kod
        self.kalkis1 = kalkis
        self.varis1 = varis
        self.sure1 = sure
        self.kapasite1 = kapasite
        self.yolcu1 = yolcu
    
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
print(ucus1.bilet_satis(5))
print(ucus1.bilet_satis(5))
print(ucus1.bilet_iptal())