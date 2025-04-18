import re
"""
cumle = 'Selam, telefon numaram 0543-4569874'
patern = '\d{3,4}-\d{7}'   #"\d\d\d\d-\d\d\d\d\d\d\d" iki ifade aynı sonucu verir

print(re.search(patern,cumle))
"""
"""
cumle = "En sevdigim kanal base42"
patern = "\s\w{5,}" #5 veya daha fazla uzunluktaki kelimeleri döndürür

for eslesme in re.finditer(patern,cumle):
    print(eslesme.group(), eslesme.span())
"""

#GSM Operatörleri
#54...   ->   Vodofone
#501,505,506   ->   AVEA
#53...   ->   Turkcell

def gsm_operator_bul(tel_no):
    patern = "(\d{3})-(\d{7})"
    eslesme = re.search(patern,tel_no)
    if eslesme:
        gsm_kod =  eslesme.groups()[0]
        if gsm_kod.startswith("54"):
            return "Vodofone"
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506"):
            return "Avea"
        elif gsm_kod.startswith("53"):
            return "Turkcell"
        else:
            return "Sebeke bulunamadi"
    else:
        return "Patern bulunamadi"

tel_no = "Selam, telefon numaram 0535-8886622"
print(gsm_operator_bul(tel_no))