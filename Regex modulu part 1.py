import re
"""
cumle = "Mustafa Kemal Atatürk, Türk asker, devlet adamı ve Türkiye Cumhuriyeti' nin kurucusudur."
patern = 'Türk'
print(re.search(patern,cumle)) #İlk Türk ifadesini döndürür
durum = re.search(patern,cumle)
print(durum.start()) #re.search ile bulduğumuz ifadenin başlangıç indisini verir
print(durum.end()) #re.search ile bulduğumuz ifadenin bitiş indisini verir
"""
"""
ornek = "En sevdiğim kanal base42"
patern2 = "base\d\d"
print(re.search(patern2,ornek))
"""

cumle = "Selam, telefon numaram 0544-5434342"
patern3 = "\d\d\d\d-\d\d\d\d\d\d\d"
print(re.search(patern3,cumle))
