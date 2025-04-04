"""
class Ucus():
    havayolu = 'THY'

ucus1 = Ucus()
print(ucus1.havayolu)
#print(Ucus().havayolu)  üstteki iki satır ile aynı işlemi yapar
"""

'''
class Ucus():
    havayolu = "THY"
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod_ = kod
        self.kalkis_ = kalkis
        self.varis_ = varis
        self.sure_ = sure
        self.kapasite_ = kapasite
        self.yolcu_ = yolcu
        
ucus2 = Ucus("TK123","DEN","IST",60,300,100)
print(ucus2.sure_)
print(ucus2.havayolu)

ucus3 = Ucus("TK245","KON","KRS",120,175,150)
print(ucus3.kod_)
print(ucus3.havayolu)
'''


class Ucus():
    havayolu = "THY"
    
    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod_ = kod
        self.kalkis_ = kalkis
        self.varis_ = varis
        self.sure_ = sure
        self.kapasite_ = kapasite
        self.yolcu_ = yolcu
        
    def anons_yap(self):
        return "{} sefer sayili {}--{} ucusumuz {} dakika sürecektir".format(
            self.kod_,
            self.kalkis_,
            self.varis_,
            self.sure_)
    
ucus4 = Ucus("TK459","BOD","ANT",40,250,250)
print(ucus4.anons_yap())


