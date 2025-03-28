# girdi = input("Bir sayi girin: ")
# print(type(girdi))      #string tipinde veri döndürür

#------------------------------------

def uygulama():
    girdi = input("Bir sayi giriniz: ")
    islem = input("Girdiginiz sayi cift mi tek mi: ")
    if islem == 'cift':
        if int(girdi)%2 == 0:
            return 'Evet cift sayidir.'
        else:
            return 'Hayir cift sayi degildir.'
    elif islem == 'tek':
        if int(girdi)%2 == 1:
            return 'Evet tek sayidir.'
        else:
            return 'Hayir tek sayi degildir.'
        
print(uygulama())

