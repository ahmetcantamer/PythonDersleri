#Parola oluşturucu örneğinde kullanıcıdan bir parola uzunluk alıcaz ve bu parolanın içinde büyük ve küçük harfler, sayılar ve semboller içericek

import random

sifre = ""
print("Oluşturmak istediğiniz parolanızın uzunluğunu giriniz: ", end ="")
pass_len = input()

words = ["qwertyuıopğüasdfghjklşizxcvbnmöç", "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ", "0123456789", ".,!'^+%&/()=?_£#${[]}\|*-"]

for i in range(int(pass_len)):

        sifre += random.choice(words[i%4])


print(sifre)